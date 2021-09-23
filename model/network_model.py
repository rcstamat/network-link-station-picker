from my_entity.device import Device
from my_entity.station import Station


class NetworkModel:
    """
        Base class for representing a model for stations and devices
    """

    def __init__(self, parser):
        self.stations = []
        self.devices = []

        for elem in parser.get_stations():
            self.stations.append(Station(elem))
        if not self.stations:
            print("No stations could be parsed from configuration file")
            exit()

        for elem2 in parser.get_devices():
            self.devices.append(Device(elem2))
        if not self.devices:
            print("No devices could be parsed from configuration file")
            exit()

    def get_max_x_with_reach(self):
        sum_x_a_reach = 0
        for station in self.stations:
            if station.get_x() + station.get_reach() > sum_x_a_reach:
                sum_x_a_reach = station.get_x() + station.get_reach()
        return sum_x_a_reach

    def get_max_y_with_reach(self):
        sum_y_a_reach = 0
        for station in self.stations:
            if station.get_y() + station.get_reach() > sum_y_a_reach:
                sum_y_a_reach = station.get_y() + station.get_reach()
        return sum_y_a_reach

    def calc_dist(self):
        pass
