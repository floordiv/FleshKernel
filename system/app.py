import modules.config as config
import importlib.util


def run(path):
    path = '../' + path[1:] if path.startswith('/') else path
    bad_functions = config.get_var('app', 'deny_functions', 'list_of_functions').split()
    bad_libs = config.get_var('app', 'deny_modules', 'list_of_modules').split()
    bad_calls = config.get_var('app', 'deny_calls', 'list_of_calls').split()
    source_vars = {}
    source_to_run = ''
    try:
        with open(f'../{path}', 'r') as source:
            source_lines = source.readlines()
            raw_source = source.read()
        for line in source_lines:

            line = __strip_line_of_comments(line)
            imports = __get_import_type(line)
            variables = __variables_from_line(line)
            if imports is not None:
                pass
            elif variables is not None:
                pass

    except Exception as executing_app_exception:
        print(f'[ERROR] An error occurred while executing app ({path}): {executing_app_exception}')


def call(func, args):
    """
    this is smth like subfunction, using by run(). All the application function calls are changing to app.call(funcname, arguments_for_func)
    """
    pass


def exists(path):
    path = '../' + path[1:] if path.startswith('/') else path
    return importlib.util.find_spec(path)


def __strip_line_of_comments(line):
    if '#' in line:
        return '#'.join(line.split('#')[:-1])
    return line


def __import_to_none(line):
    import_type = __get_import_type(line)[0]
    import_name_index = __module_to_import(line, __get_import_type(line))[2]
    where_is_import = __get_import_type(line)[1]
    if import_type == 'static':
        line = line[:where_is_import[1] + 1] + 'none'
    else:
        # so, here we should paste the none lib inside of the line
        line = line[:import_name_index[0]] + 'none' + line[import_name_index[1] - 1:]

    return line


def __module_to_import(line, import_info):
    importing_type = None
    importing_module = ''
    equation_start = import_info[1][1] + 1
    indexes = []
    counter = 0
    if line[equation_start] in ['\'', '"']:
        importing_type = 'str'

        indexes.append(equation_start + 1)
        counter = equation_start + 1
        for symbol in line[equation_start + 1:]:
            if symbol not in ['\'', '"']:
                importing_module += symbol
                counter += 1
        indexes.append(counter)
    else:
        importing_type = 'var'

        indexes.append(equation_start)
        counter = equation_start
        for symbol in line[equation_start:]:
            if symbol != ')':
                importing_module += symbol
                counter += 1

        indexes.append(counter)

    if import_info[0] == 'static':
        importing_type = 'name'

    return [importing_type, importing_module, indexes]


def __get_import_type(line):
    types = {
        'import': 'static',
        'from': 'static',
        '__import__': 'dynamic',
        'importlib': 'dynamic',
        'import_module(': 'dynamic'
    }

    elements = {}
    for element in types:
        if element in line:
            elements[element] = [line.find(element), line.find(element) + len(element)]

    if elements is []:
        return None

    return [types[max(elements, key=len)], elements[max(elements, key=len)]]  # import type, indexes of import (word), import method


# this functions made by telegram user @SleepingKitty0
def __replace_braces(text, toreplace='()[]{}'):
    string_indent = '\'', '"'
    is_string = False
    lst = list(text)
    functions = []
    characters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_')
    current_ident = None
    for char in enumerate(text):
        index, char = char
        if char in '()' and lst[index - 1] in characters:
            is_string = not is_string

            functions.append(index)
        if char in string_indent and not is_string:
            is_string = not is_string
            current_ident = char
        if char == current_ident and is_string:
            is_string = None
            current_ident = None
        if char in toreplace and not is_string:
            lst[index] = ''
    return ''.join(lst), functions


# this functions made by telegram user @SleepingKitty0
def __grep(text):
    string_ident = '\'', '"'
    current_ident = None
    positions = []
    is_string = False
    for n in enumerate(text):
        index, value = n
        if not is_string and value in string_ident:
            current_ident = value
            is_string = True
            positions.append([index, None])
        elif is_string and value == current_ident:
            positions[-1][1] = index + 1
            is_string = False

    if is_string:
        raise SyntaxError('missed string quote')
    return positions


# this functions made by telegram user @SleepingKitty0
def __split2(text, splitby=','):
    string_ident = '\'', '"'
    out = []
    temp = ""
    is_string = False
    current_indent = None
    for n in enumerate(text):
        index, char = n
        # print(index)
        try:
            if is_string and char == current_indent:
                is_string = False
                temp += current_indent
                current_indent = None
                continue
            elif not is_string and char in string_ident:
                is_string = True
                current_indent = char
                temp += char
            elif is_string and char != current_indent:
                temp += char
            elif not is_string and char == splitby:
                out.append(temp)
                temp = ""
            elif not is_string and char != splitby:
                temp += char
        except IndexError:
            pass
    if len(temp) is not None:
        out.append(temp)

    for each in enumerate(out):
        if each[1][0] == ' ':
            out[each[0]] = each[1][1:]

    return out


def __variables_from_line(line):
    if line.strip().split('=')[1] == '':  # if we will split line "var==me", we will get ['var', '', 'me']
        return None
    else:
        split_text = __split2(line)
        if '=' in split_text[0]:
            variable_name = [split_text[0].split('=')[0].strip()]
            variable_content = split_text[0].split('=')[1:] + split_text[1:]
        else:
            finished = False
            variable_name = []
            last_index = 0

            for local_index, each in enumerate(split_text):
                if finished:
                    break
                if finished is False and '=' in each:
                    variable_name.append(each.split('=')[0])
                    last_index = local_index
                    finished = True
                elif finished is False:
                    variable_name.append(each)
            variable_content = split_text[last_index].split('=')[1:] + split_text[last_index + 1:]
    for index, each in enumerate(variable_name):
        local_each = each
        if each.startswith(' '):
            local_each = local_each[1:]
        if each.endswith(' '):
            local_each = local_each[:-1]
        variable_name[index] = local_each

    for var_index, var_each in enumerate(variable_content):
        local_each = var_each
        if var_each.startswith(' '):
            local_each = local_each[1:]
        if var_each.endswith(' '):
            local_each = local_each[:-1]
        variable_content[var_index] = local_each

    return variable_name, variable_content


def __get_functions_calls(splitted_line):
    characters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_')
    functions = {}
    temp = []
    function_arguments = False
    for index, each in enumerate(splitted_line):
        # last_character = splitted_line[index - 1] in characters
        if '(' in each and not function_arguments and splitted_line[index + 1] == ')':
            func_name = temp
            functions[func_name] = None
            temp = []
        if ')' not in each and function_arguments:
            temp.append(each)
        if '(' in each and not function_arguments:
            function_arguments = True
            temp = [each]
        if ')' in each and function_arguments:
            temp.append(each)
            func_name = temp[0].split('(')[0]
            if func_name not in functions:
                functions[func_name] = []
            for element in temp:
                if element.endswith(')'): element = element[:-1]
                if '(' in element: element = element.split('(')[1]
                functions[func_name].append(element)
            function_arguments = False
    for each in functions:
        if functions[each][0] == functions[each][1]:
            del functions[each][1]
        if functions[each][0] == '':
            functions[each][0] = None
    return functions


print(__replace_braces('world, var = (hello), ((get_lines())), (go_fuck(some_arg1, some_arg2, a, b)), "worlder, yes"')[0])
print('\n\n')
print(__variables_from_line('world, var = (hello), ((get_lines())), (go_fuck(some_arg1, some_arg2, a, b)), "worlder, yes"'))
print(__variables_from_line('world, var = hello, get_lines(), go_fuck(some_arg1, some_arg2, a, b), "worlder, yes"'))
print(__get_functions_calls(__variables_from_line('world, var = hello, get_lines(), go_fuck(some_arg1, some_arg2, a, b), "worlder, yes"')[1]))
# print(__get_functions_calls('hello, world(hi, world)'.split(',')))
# print(__variables_from_line('var = test, "hello, worlder"'))

