from coordinate_entity import CoordinateEntity


class Device(CoordinateEntity):
    def __init__(self, device_list=None):
        try:
            self.x = device_list[0]
            self.y = device_list[1]

        except (IndexError, TypeError):
            print("Device {} has invalid attributes. Must have 2 coordinates x axis, y axis".format(
                device_list))
            exit(0)

    def get_all(self):
        return [self.x, self.y]
