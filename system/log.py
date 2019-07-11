import os
import settings
import func


def init():
    global is_initialized
    is_initialized = True
    write('__init', )


def write(log_type, text, show_time=True, show_date=True, show_type=True, subtype=None):
    if is_initialized:
        if log_type == '__init':
            show_type = None
            show_time = None
            show_date = None

        if log_type not in settings.log.files:
            pass

        existing_files = []
        others = []

        for file in settings.log.files[log_type]:   # sorting of existing log files and non-existing
            if os.path.exists(file):
                existing_files.append(file)
            else:
                others.append(file)

        if log_type == '__init':
            line = text
        line = f'[{log_type.upper()}] []'    # creating line

        for log_file in existing_files:
            if log_file.strip() == '':      # if element (filename) is empty, continue working
                pass
            else:
                with open(log_file, 'a') as file:
                    file.write(f'\n{"-" * 30}')     # new line and text
    else:
        init()
