import os
import json

class JsonParser():
    """
        Parse json input files
    """

    def __init__(self, input_file, input_folder):
        file_rel_path = os.path.join(input_folder, input_file)
        with open(file_rel_path, 'r') as json_file:
            json_data = json_file.read()
        try:
            self.data = json.loads(json_data)
        except Exception:
            print("There was an error parsing the input json file")
            exit(0)

    def get_stations(self):
        try:
            return self.data["stations"]
        except KeyError:
            print("There are no stations defined in the input file")
            exit(0)

    def get_devices(self):
        try:
            return self.data["devices"]
        except KeyError:
            print("There are no devices defined in the input file")
            exit(0)
