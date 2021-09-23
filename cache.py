import pickle
from os.path import exists


class Cache:
    """
        Dictionary based cache that is being stored on disk
    """

    def __init__(self, cache_file):
        self.cache_file = cache_file
        self.cache = {}
        objects = []

        if exists(self.cache_file):
            with open(self.cache_file, "rb+") as f:
                while True:
                    try:
                        objects.append(pickle.load(f))
                    except EOFError:
                        break
            for x in objects:
                for y in x:
                    self.cache[y] = x[y]
        else:
            open(cache_file, 'w').close()

    @staticmethod
    def invalidate(cache_file):
        open(cache_file, 'w').close()

    def put_map(self, key, value):
        self.cache[key] = value

    def get_map(self, key):
        if key in self.cache:
            return self.cache[key]

    def save_to_file(self, cache_file):
        with open(cache_file, "wb+") as f:
            if self.cache:
                pickle.dump(self.cache, f)
