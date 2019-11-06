import modules.encryption as encryption
import modules.file_system as fs
import modules.line_parser as parser
import modules.errors as err
import modules.log as log
import os
import sys
import json
import app
import memory
import func
import user
import socket
import errno


# default sockets for kernel modules starts with 12076


class application:
    @staticmethod
    def run(appname, args,):
        pass

    @staticmethod
    def runcmd(line):
        pass

    @staticmethod
    def info(appname, from_program):    # from_program - name of the requesting app, for access controlling
        pass


def json_content(file, allow_multiple_dicts=False, from_config=True):
    try:
        if from_config:
            file = '../cfg/' + file
        with open(file, 'r') as json_file:
            if not allow_multiple_dicts:
                return json.load(json_file)[0]
            else:
                return json.load(json_file)
    except FileNotFoundError:
        return None


def init():
    # check configs
    required_configs = ['kernel', 'memory', 'sandbox', 'screen', 'keyboard']
    given_configs = os.listdir('../cfg')
    missing_configs = []
    for each in required_configs:
        if each not in given_configs:
            missing_configs.append(each)
    for each in required_configs:
        try:
            with open('../cfg/' + each, 'r') as cfg:
                json.load(cfg)
        except:
            if each not in missing_configs:
                missing_configs.append(each)
    if len(missing_configs) > 0:
        print(f'[ERROR] Missing or corrupted configs: {", ".join(missing_configs)}')
        set_to_default = input('Set this configs to default? [y/n] > ')
        if set_to_default.lower().strip() == 'y':
            default_values = {
                'kernel': {

                },
                'memory': {

                },
                'file_system': {
                    'directory': {
                        'guest': {
                            'list_type': 'whitelist',
                            'func_list': [''],
                            'dir_list': ['']    # log
                        },
                        'user': {
                            'list_type': 'whitelist',
                            'func_list': [''],
                            'dir_list': ['']
                        }
                    }
                },
                'sandbox': {

                },
                'screen': {
                    'resolution': '55x200',
                    'input': 'keyboard.input',
                    'output': 'keyboard.output'
                },
                'keyboard': {

                }
            }
            for each in default_values:
                print(f'[INFO] Setting config "{each}" to default...')
                with open('../cfg/' + each, 'w') as config:
                    json.dump([default_values[each]], config)
                print(f'[INFO] Config "{each}" set to default successfully')
    else:
        print('[INFO] All configs seems to be good')
    # init modules paths
    try:
        paths = json_content('kernel')['paths']
        print('[INFO] Successfully read paths for initializing')
    except Exception as exception_reading_paths:
        paths = ['..user/programs', 'modules', 'drivers']
        print('[ERROR] Failed to read paths to initialize. Using default...')
    for path in paths:
        sys.path.insert(0, path)
    print('[INFO] Paths initialized successfully')


def deinit():
    pass


init()


# very very bad person, and python hater: telegram - @barmatographOS. FUck you, idiot, py one love!
