from network_model import NetworkModel
import math


class NetworkModel1(NetworkModel):
    """
        Solution model where the distance is being calculated everytime by measuring the distance between each device
        and each station
    """

    def __init__(self, parser):
        NetworkModel.__init__(self, parser)

    def calc_dist(self):
        output = []
        for device in self.devices:
            solution = []
            for station in self.stations:
                dist = int(math.sqrt((device.get_x() - station.get_x()) ** 2 + (device.get_y() - station.get_y()) ** 2))
                reach = station.get_reach()
                if dist > reach:
                    power = 0
                else:
                    power = (reach - dist) ** 2
                    if power > 0:
                        if not solution or solution[2] < power:
                            solution = [station.get_x(), station.get_y(), power]

            if solution:
                output.append("Best link station for point {0},{1} is {2},{3} with power {4}".format(device.get_x(),
                                                                                                     device.get_y(),
                                                                                                     solution[0],
                                                                                                     solution[1],
                                                                                                     solution[2]))

            else:
                output.append("No link station within reach for point {0},{1}".format(device.get_x(), device.get_y()))
        return output
