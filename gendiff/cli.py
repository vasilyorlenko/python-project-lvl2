import argparse

parser = argparse.ArgumentParser(description='Generate diff', prog='gendiff')
parser.add_argument('filepath1')
parser.add_argument('filepath2')
parser.add_argument(
    '-f',
    '--format',
    default='default',
    help='set format of output',
)
