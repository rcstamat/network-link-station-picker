class Cell:
    """
        Power map unit
    """
    def __init__(self, station_owner_id=0, is_station=False, power=0):
        self.station_owner_id = station_owner_id
        self.is_station = is_station
        self.power = power
