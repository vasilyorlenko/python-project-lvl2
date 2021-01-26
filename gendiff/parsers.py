from os import path
from json import load

from yaml import safe_load

parsers = {
    '.yaml': safe_load,
    '.yml': safe_load,
    '.json': load,
}


def get_parser(path_to_file):
    _, ext = path.splitext(path_to_file)

    return parsers[ext]
