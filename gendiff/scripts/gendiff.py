#!usr/bin/env python

from gendiff.cli import parser
from gendiff.gendiff import generate_diff


def main():
    args = parser.parse_args()
    print(generate_diff(args.filepath1, args.filepath2, args.format))


if __name__ == '__main__':
    main()
