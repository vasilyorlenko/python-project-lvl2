from json import dumps

from gendiff.format.default import format_default
from gendiff.format.plain import format_plain

formatters = {
    'stylish': format_default,
    'plain': format_plain,
    'json': dumps,
}


def get_formatter(format_type):
    if format_type not in formatters:
        raise Exception('Unknown format: {0}'.format(format_type))

    return formatters[format_type]
