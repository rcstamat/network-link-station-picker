from colorama import Fore, Style
from cell import Cell
import math


class PowerMap:
    """
        A matrix that maps power to stations
    """

    def __init__(self, x, y, stations, devices):
        self.x = x
        self.y = y
        self.stations = stations
        self.devices = devices
        self.power_map = []
        self.TEXT_COLOR = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.LIGHTBLUE_EX,
                           Fore.LIGHTMAGENTA_EX,
                           Fore.MAGENTA, Fore.LIGHTRED_EX]

    def init_power_map(self):
        self.power_map = [None] * self.x
        for u in range(0, self.x):
            self.power_map[u] = [None] * self.y
        for i in range(0, self.x):
            for j in range(0, self.y):
                self.power_map[i][j] = Cell(0, False, 0)

    def create_power_map(self):
        self.init_power_map()
        station_id = 1
        for station in self.stations:
            for i in range(0, self.x):
                for j in range(0, self.y):
                    station_x = station.get_x()
                    station_y = station.get_y()

                    # station cell
                    if i == station_x and j == station_y:
                        self.power_map[i][j].is_station = True
                    else:
                        if not self.power_map[i][j].is_station:
                            self.power_map[i][j].is_station = False

                    # modify cell if the current station has more power
                    dist = int(math.sqrt((station_x - i) ** 2 + (station_y - j) ** 2))
                    power = (station.reach - dist) ** 2
                    if dist - station.reach <= 0:
                        if self.power_map[i][j].power < power:
                            self.power_map[i][j].power = power
                            self.power_map[i][j].station_owner_id = station_id
            station_id = station_id + 1

    def rotate_matrix_90_anticlockwise(self, matrix):
        # debug method
        temp = [None] * self.x
        for u in range(0, self.x):
            temp[u] = [None] * self.y
        for i in range(0, self.x):
            for j in range(0, self.y):
                temp[self.x - j - 1][i] = matrix[i][j]

        return temp

    def print_power_map(self, power_map):
        # debug method
        print("Reach map")
        for i in range(0, self.x):
            for j in range(0, self.y):
                print(self.TEXT_COLOR[power_map[i][j].station_owner_id % len(self.TEXT_COLOR)] + str(
                    power_map[i][j].station_owner_id), end=' ')
            print("")

        print(Style.RESET_ALL)
        print("Power map")
        FORMAT_SIZE = 4
        for i in range(0, self.x):
            for j in range(0, self.y):
                p = power_map[i][j].power
                size = len(str(p))
                print(self.TEXT_COLOR[power_map[i][j].station_owner_id % len(self.TEXT_COLOR)] + str(power_map[i][j].power),
                      end=' ' * max(1, FORMAT_SIZE - size))
            print("")
        print("" + Style.RESET_ALL)

        print(Style.RESET_ALL)
        print("Station owner map")
        for i in range(0, self.x):
            for j in range(0, self.y):
                if power_map[i][j].is_station:
                    print(self.TEXT_COLOR[power_map[i][j].station_owner_id % len(self.TEXT_COLOR)] + "1", end=' ')
                else:
                    print(self.TEXT_COLOR[power_map[i][j].station_owner_id % len(self.TEXT_COLOR)] + "0", end=' ')
            print("")
        print("" + Style.RESET_ALL)
