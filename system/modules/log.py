import os
import modules.config as config
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


def file_exists(name):
    homepath = memory.read('homepath', name='kernel')
    if name in os.listdir(f'{homepath}/log'):
        return True
    return False
