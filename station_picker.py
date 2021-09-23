import sys
sys.path.append('model')
sys.path.append('my_entity')
sys.path.append('file_parser')

from file_parser.json_parser import JsonParser
from cache import Cache
from argparse import ArgumentParser
from model.network_model_1 import NetworkModel1
from model.network_model_2 import NetworkModel2


def main(args):
    INPUT_FOLDER = "input"

    if args.network_model == 'NetworkModel1':
        print_list(NetworkModel1(JsonParser(args.input_file, INPUT_FOLDER)).calc_dist())
    elif args.network_model == 'NetworkModel2':
        cache = None
        if args.invalidate_cache:
            Cache.invalidate("cache")
        if args.caching:
            cache = Cache("cache")
        print_list(NetworkModel2(JsonParser(args.input_file, INPUT_FOLDER), cache).calc_dist())
    else:
        print("Chose between NetworkModel1 or NetworkModel2")


def print_list(input_list):
    for elem in input_list:
        print(elem)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('input_file', type=str,
                        help='input_file')
    parser.add_argument('--model', dest='network_model', type=str,
                        help='network_model', default='NetworkModel1')
    parser.add_argument('--caching', dest='caching', type=bool,
                        help='caching', default=True)
    parser.add_argument('--invalidate_cache', dest='invalidate_cache', type=bool,
                        help='invalidate_cache', default=False)
    args = parser.parse_args()
    main(args)
