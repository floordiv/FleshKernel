import modules.cryptography as encryption
import modules.file_system as fs
import modules.line_parser as parser
import modules.log as log
import cfg
import os
import sys
import json
import random

import app
import errors
import memory
import func
import user
import socket
import errno


class modules:
    pass


class drivers:
    __drivers = {}  # {driver_name: {kwargs}}

    @staticmethod
    def append(name, driver_type, caller):
        pass

    @staticmethod
    def remove(name, caller):
        pass

    @staticmethod
    def set_active(name, caller):
        pass

    @staticmethod
    def listing(caller):
        log.write('drivers', caller, 'info', f'{caller}: get list of drivers')
        return list(drivers.__drivers.keys())

    @staticmethod
    def info(target, caller):
        log.write('drivers', caller, 'info', f'{caller}: get info about driver {target}')
        return drivers.__drivers[target]

    @staticmethod
    def infos(caller):
        log.write('drivers', caller, 'info', f'{caller}: get information of all drivers')
        return drivers.__drivers

    @staticmethod
    def _valid_inf(name, caller):
        func_temp_id = random.random()
        log.write('drivers', caller, 'info', f'{caller}: validating .inf file for driver {name} (id:{func_temp_id})')
        required_vars = cfg.json_content('kernel_drivers')
        given_vars = drivers._get_details(name)
        missing = []
        for each in given_vars:
            if each not in required_vars:
                missing.append(each)
        if len(missing) == 0:
            log.write('drivers', caller, 'info', f'{caller}: validating .inf file for driver {name} (id:{func_temp_id})'
                                                 ' completed successfully')
            return True
        log.write('drivers', caller, 'info', f'{caller}: validating .inf file for driver {name} (id:{func_temp_id})'
                                             f' completed; missing variables: {", ".join(missing)}')
        return missing

    @staticmethod
    def _get_details(name, caller):
        log.write('drivers', caller, 'info', f'{caller}: get detail info of driver {name}')
        files = os.listdir('drivers')
        if name + '.py' not in files or name + '.inf' not in files:
            return None
        with open('drivers/' + name + '.inf', 'r') as info_file:
            info = info_file.read().split('\n')
        result = {}
        for each in info:
            content = each.split('=')
            result[content[0]] = '='.join(content[1:])
            result[content[0]] = result[content[0]].strip("'")

        # remove spaces before and after var names and values
        for element in list(result.keys()):
            new_temp = element
            if element.startswith(' '):
                new_temp = new_temp[1:]
            if element.endswith(' '):
                new_temp = new_temp[:-1]
            if element != new_temp:
                result[new_temp] = result[element]
                del result[element]
        for element in list(result.keys()):
            name = element
            element = result[element]
            new_temp = element[1:]
            if element.startswith(' '):
                new_temp = new_temp[1:]
            if element.endswith(' '):
                new_temp = new_temp[:-1]
            if element != new_temp:
                result[name] = new_temp
        return result


class actions:
    @staticmethod
    def live_log(write=True):
        pass


class proc:
    __listing = {}
    __permissions = {}

    @staticmethod
    def listing(caller):
        pass


def init():
    # get modules aliases
    cfg.json_content()
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
                            'dir_list': [['/root/log', 'path', 'ro'], ['/root/cfg', 'path'], ['/root/system/modules', 'path'], ['/root/system/app.py', 'file'],
                                         ['/root/system/func.py', 'file'], ['/root/system/memory.py', 'file'], ['/root/system/user.py', 'file']]
                        },
                        'user': {
                            'list_type': 'whitelist',
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
        paths = cfg.json_content('kernel')['paths']
        print('[INFO] Successfully read paths for initializing')
    except Exception as exception_reading_paths:
        paths = ['..user/programs', 'modules', 'drivers']
        print('[ERROR] Failed to read paths to initialize. Using default...')
    for path in paths:
        sys.path.insert(0, path)
    print('[INFO] Paths initialized successfully')


# init()


# very very bad person, and python hater: telegram - @barmatographOS. FUck you, idiot, py one love!
