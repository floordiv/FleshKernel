import re


def parse(text, config):
    argument_prefix = config['prefix']
    subargument_prefix = config['sub_prefix']
    argument_split = config['split']
    result = {'nonarguments': [], 'arguments': [], 'sub_arguments': [], 'objects': {}}
    text_split = text.split(argument_split)
    tmp_object = {'result': '', 'state': 1}
    start_index = 0
    in_quotes = False
    for element in text_split:
        if element.strip() == '':
            continue
        if re.match(subargument_prefix, element) is not None:
            if not in_quotes:
                result['sub_arguments'].append(''.join(element[len(subargument_prefix):]))
            else:
                tmp_object['result'] += ''.join(element) + ' '
        elif re.match(argument_prefix, element) is not None:
            if not in_quotes:
                result['arguments'].append(''.join(element[len(argument_prefix):]))
            else:
                tmp_object['result'] += ''.join(element) + ' '
        elif element[0] == '"' and element[-1] == '"':
            result['objects'][''.join(text_split[text_split.index(element) - 1])] = ''.join(element[1:-1])
        elif element[0] == '"':
            start_index = text_split.index(element) - 1
            in_quotes = True
            if tmp_object['state'] == 1:
                tmp_object['state'] = 0
                tmp_object['result'] += ''.join(element[1:]) + ' '
        elif element[-1] == '"':
            if tmp_object['state'] == 0:
                tmp_object['result'] += ''.join(element[:-1])
            tmp_object['state'] = 1
            result['objects'][text_split[start_index]] = tmp_object['result']
            tmp_object['result'] = ''
            in_quotes = False
        else:
            if not in_quotes:
                result['nonarguments'].append(element)
            else:
                tmp_object['result'] += ''.join(element) + ' '
    return result
