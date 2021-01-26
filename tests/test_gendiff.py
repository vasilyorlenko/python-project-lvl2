from os import path, getcwd

from pytest import raises

from gendiff.gendiff import generate_diff


def get_fixture_path(filename):
    return path.join(getcwd(), 'tests', 'fixtures', filename)


json_path1 = get_fixture_path('file1.json')
json_path2 = get_fixture_path('file2.json')
yaml_path1 = get_fixture_path('file1.yaml')
yaml_path2 = get_fixture_path('file2.yaml')

with open(get_fixture_path('default.txt')) as reader:
    expected_default = reader.read()

with open(get_fixture_path('plain.txt')) as reader:
    expected_plain = reader.read()

with open(get_fixture_path('json.txt')) as reader:
    expected_json = reader.read()


def test_json():
    assert generate_diff(json_path1, json_path2) == expected_default
    assert generate_diff(json_path1, json_path2, 'plain') == expected_plain
    assert generate_diff(json_path1, json_path2, 'json') == expected_json


def test_yaml():
    assert generate_diff(yaml_path1, yaml_path2) == expected_default
    assert generate_diff(yaml_path1, yaml_path2, 'plain') == expected_plain
    assert generate_diff(yaml_path1, yaml_path2, 'json') == expected_json


def test_mixed():
    assert generate_diff(json_path1, yaml_path2) == expected_default
    assert generate_diff(yaml_path1, json_path2) == expected_default


def test_invalid_format_behavior():
    with raises(Exception):
        generate_diff(json_path1, json_path2, 'wrong')
