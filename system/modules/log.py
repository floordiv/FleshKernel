import os
import cfg
import func


def write(name, caller, text_type, text):
    current_time = func.current.time
    current_date = func.current.date
    homepath = cfg.json_content('log')
    if not file_exists(name):
        open(f'{homepath}/log/{name}', 'w').close()
    with open(f'{homepath}/log/{name}', 'a') as log_file:
        info_chunk = f'[{caller}] [{text_type.upper()}] [{current_date} {current_time}]'
        line = f'{info_chunk}  {text}\n'
        log_file.write(line)

        return 'line-written-successfully'


def file_exists(name):
    homepath = cfg.json_content('log')
    if name in os.listdir(f'{homepath}/log'):
        return True
    return False

