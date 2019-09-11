import os
import config
import func
import memory


"""
valid log file:
first line is metadata
required variables for valid metadata: created, last_edit, last_edit_line, total_lines   UPDATED: some of this vars are not required anymore
"""


def write(name, text_type, text):
    current_time = func.current.time
    current_date = func.current.date
    homepath = config.get_var('log', 'paths', 'homepath')
    if not file_exists(name):
        open(f'{homepath}/log/{name}', 'w').close()
    with open(f'{homepath}/log/{name}', 'a') as log_file:
        info_chunk = f'[{text_type.upper()} {current_date} {current_time}]'
        line = f'{info_chunk}  {text}\n'
        log_file.write(line)

        return 'line-written-successfully'


# def create(name, **additional_vars):
#     required_varables_for_first_log_file = config.getvar('log', 'vars', 'required_vars_for_valid_log').strip().split('|')
#     dict_of_variables = []
#
#     for element in additional_vars:
#         required_varables_for_first_log_file.append(f'{element}:{app.log_var_types[additional_vars[element]]()}')
#
#     for element in required_varables_for_first_log_file:
#         # if element == 'created':
#         #     dict_of_variables.append(f'created:{app.log_var_types[required_varables_for_first_log_file["created"]]()}')
#         #     continue
#         dict_of_variables.append(f'{element}:{app.log_var_types[required_varables_for_first_log_file[element]]()}')
#
#     first_line = '|'.join(dict_of_variables)
#
#     with open(f'{app.homepath}/log/{name}', 'w') as open_file:
#         open_file.write(first_line)
#
#     return 'new-log-file-created-successfully'


# def edit(name, line, new_text):
#     if valid(name):
#         with open(f'{app.homepath}/log/{name}', 'r') as log_file:
#             current_log = log_file.readlines()
#
#         current_log[line] = new_text
#
#         # edit first line
#         first_line = current_log[0].strip().split('|')
#
#         with open(f'{app.homepath}/log/{name}', 'w') as save_log:
#             save_log.write('\n'.join(current_log))
#
#         return 'saved-successfully'
# 
#     return False


# def get_metadata(name):
#     first_line_data = open(f'{app.homepath}/log/{name}', 'r').readlines()[0].split('|')
#     vars_in_current_first_line = {}
#
#     for element in first_line_data:
#         vars_in_current_first_line[element.strip().split(':')[0]] = element.split(':')[1]
#
#     return vars_in_current_first_line       # returns dict
#
#
# def edit_metadata(name, new_data):
#     metadata = get_metadata(name)
#     string_metadata = []
#
#     for element in metadata:
#         if element in new_data:
#             metadata[element] = new_data[element]
#
#     for var in metadata:
#         string_metadata.append(f'{var}:{metadata[var]}')
#
#     return edit(name, 1, '|'.join(string_metadata))
#
#
# def valid(name):
#     if file_exists(name):
#         required_varables_for_first_log_file = config.getvar('log', 'vars', 'required_vars_for_valid_log')
#         config_valid = None
#
#         for element in get_metadata(name):
#             if element in required_varables_for_first_log_file:
#                 config_valid = True
#             else:
#                 config_valid = False
#                 continue
#         return config_valid
#     return False


def file_exists(name):
    homepath = memory.read('homepath', name='kernel')
    if name in os.listdir(f'{homepath}/log'):
        return True
    return False
