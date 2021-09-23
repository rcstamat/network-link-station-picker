from coordinate_entity import CoordinateEntity


class Station(CoordinateEntity):
    def __init__(self, station_list=None):
        try:
            self.x = station_list[0]
            self.y = station_list[1]
            self.reach = station_list[2]
        except (IndexError, TypeError):
            print("Station {} has invalid attributes. Must have 3 coordinates x axis, y axis, r reach".format(
                station_list))
            exit(0)

    def get_all(self):
        return [self.x, self.y, self.reach]

    def get_reach(self):
        return self.reach

    def to_string(self):
        return str(self.x) + "_" + str(self.y) + "_" + str(self.reach)
