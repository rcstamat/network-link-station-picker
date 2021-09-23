from power_map import PowerMap
from network_model import NetworkModel
from hashlib import md5
import pickle


class NetworkModel2(NetworkModel):
    """
        Solution model where a map of power to station is precalculated in order for fast device selections. It can
        cache this map for future invocations
    """

    def __init__(self, parser, cache=None):
        NetworkModel.__init__(self, parser)
        self.max_x = self.get_max_x_with_reach()
        self.max_y = self.get_max_y_with_reach()
        self.cache = cache
        self.power_map = PowerMap(self.max_x, self.max_y, self.stations, self.devices)
        self.init_power_map()

        # debug
        # self.tmp = self.power_map.rotate_matrix_90_anticlockwise(self.power_map.power_map)
        # self.power_map.print_power_map(self.tmp)

    def init_power_map(self):
        if self.cache:
            stations_hash = self.create_stations_hash()
            encoded_map = self.cache.get_map(stations_hash)

            if encoded_map:
                try:
                    power_map = pickle.loads(encoded_map)
                except pickle.UnpicklingError:
                    print("Could not serialise the power map from the cache")
                    exit(0)
                self.power_map.power_map = power_map

        if not self.power_map.power_map:
            self.power_map.create_power_map()
        if self.cache:
            stations_hash = self.create_stations_hash()
            power_map = pickle.dumps(self.power_map.power_map)
            self.cache.put_map(stations_hash, power_map)
            self.cache.save_to_file(self.cache.cache_file)

    def create_stations_hash(self):
        final_string = ''
        for station in self.stations:
            final_string = final_string + station.to_string()
        return md5(final_string.encode('utf-8')).hexdigest()

    def calc_dist(self):
        for device in self.devices:
            device_x = device.get_x()
            device_y = device.get_y()

            if device_x < self.max_x and device_y < self.max_y:
                device_cell = self.power_map.power_map[device_x][device_y]
                if device_cell.power == 0:
                    print("No link station within reach for point {0},{1}".format(device_x, device_y))
                    continue
                print("Best link station for point {0},{1} is {2},{3} with power {4}".format(device_x, device_y,
                                                                                             self.stations[
                                                                                                 device_cell.station_owner_id - 1].get_x(),
                                                                                             self.stations[
                                                                                                 device_cell.station_owner_id - 1].get_y(),
                                                                                             device_cell.power))
            else:
                print("No link station within reach for point {0},{1}".format(device.get_x(), device.get_y()))
