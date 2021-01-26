from os.path import abspath

from gendiff.parsers import get_parser
from gendiff.format import get_formatter


def build_diff(parsed_file1, parsed_file2):
    keys_union = parsed_file1.keys() | parsed_file2.keys()
    keys = sorted(list(keys_union))

    def process_key(key):
        if key not in parsed_file2:
            return {
                'node_type': 'removed',
                'key': key,
                'value': parsed_file1[key],
            }

        if key not in parsed_file1:
            return {
                'node_type': 'added',
                'key': key,
                'value': parsed_file2[key],
            }

        oldValue = parsed_file1[key]
        newValue = parsed_file2[key]

        if oldValue == newValue:
            return {'node_type': 'unchanged', 'key': key, 'value': oldValue}

        if not isinstance(oldValue, dict) or not isinstance(newValue, dict):
            return {
                'node_type': 'updated',
                'key': key,
                'value': (oldValue, newValue),
            }

        return {
            'node_type': 'nested',
            'key': key,
            'children': build_diff(oldValue, newValue),
        }

    diff = list(map(process_key, keys))

    return diff


def generate_diff(first_filepath, second_filepath, format_type='default'):
    file1 = open(abspath(first_filepath), 'r')
    file2 = open(abspath(second_filepath), 'r')
    parsed_file1 = get_parser(first_filepath)(file1)
    parsed_file2 = get_parser(second_filepath)(file2)

    diff = build_diff(parsed_file1, parsed_file2)
    formatted_diff = get_formatter(format_type)(diff)

    return formatted_diff
