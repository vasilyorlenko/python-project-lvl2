def format_value(value):
    if type(value) is bool:
        return str(value).lower()

    if value is None:
        return 'null'

    if isinstance(value, dict):
        return '[complex value]'

    return "'{0}'".format(value) if type(value) is str else value


def process_node(node, path, iterate):
    node_type = node['node_type']
    key = node['key']

    if node_type == 'removed':
        return "Property '{0}{1}' was removed".format(path, key)

    if node_type == 'added':
        return "Property '{0}{1}' was added with value: {2}".format(
            path,
            key,
            format_value(node['value']),
        )

    if node_type == 'unchanged':
        return ''

    if node_type == 'updated':
        return "Property '{0}{1}' was updated. From {2} to {3}".format(
            path,
            key,
            format_value(node['value'][0]),
            format_value(node['value'][1]),
        )

    if node_type == 'nested':
        return iterate(node['children'], path + key)


def iterate(current, property_path):
    path = property_path and '{0}.'.format(property_path)
    items = [process_node(node, path, iterate) for node in current]
    filtered_items = filter(lambda item: item, items)

    return '\n'.join(filtered_items)


def format_plain(diff):
    return iterate(diff, '')
