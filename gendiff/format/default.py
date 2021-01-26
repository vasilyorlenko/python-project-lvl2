SPACES_PER_INDENT_LEVEL = 4


def format_value(current_value, indent_level):
    if current_value is None:
        return 'null'

    if type(current_value) is bool:
        return str(current_value).lower()

    if not isinstance(current_value, dict):
        return str(current_value)

    padding = SPACES_PER_INDENT_LEVEL * indent_level

    lines = [
        (' ' * padding)
        + '{0}: {1}'.format(key, format_value(value, indent_level + 1))
        for key, value in current_value.items()
    ]

    return '{{\n{0}\n{1}}}'.format(
        '\n'.join(lines),
        (' ' * (padding - SPACES_PER_INDENT_LEVEL)),
    )


def pad_start(string, target_length):
    string_length = len(string)
    if target_length <= string_length:
        return string

    return (' ' * (target_length - string_length)) + string


def process_node(node, iterate, padding, indent_level):
    node_type = node['node_type']
    key = node['key']

    if node_type != 'nested':
        value = node['value']

    if node_type == 'removed':
        return (
            pad_start('- ', padding)
            + '{0}: {1}'.format(key, format_value(value, indent_level + 1))
        )

    if node_type == 'added':
        return (
            pad_start('+ ', padding)
            + '{0}: {1}'.format(key, format_value(value, indent_level + 1))
        )

    if node_type == 'unchanged':
        return (
            (' ' * padding)
            + '{0}: {1}'.format(key, format_value(value, indent_level + 1))
        )

    if node_type == 'updated':
        return (
            pad_start('- ', padding)
            + '{0}: {1}'.format(key, format_value(value[0], indent_level + 1))
            + '\n'
            + pad_start('+ ', padding)
            + '{0}: {1}'.format(key, format_value(value[1], indent_level + 1))
        )

    if node_type == 'nested':
        return (
            (' ' * padding)
            + '{0}: {{\n{1}\n{2}}}'.format(
                key,
                iterate(node['children'], indent_level + 1),
                ' ' * padding,
            )
        )


def iterate(current, indent_level):
    padding = SPACES_PER_INDENT_LEVEL * indent_level

    lines = [
        process_node(node, iterate, padding, indent_level)
        for node in current
    ]

    return '\n'.join(lines)


def format_default(diff):
    return '{\n' + iterate(diff, 1) + '\n}'
