import time
import os
import json


def check_config():
    result = None
    if os.path.isfile('cfg/boot'):
        try:
            with open('cfg/boot') as boot_conf:
                content = json.load(boot_conf)[0]
                for each in required_variables:
                    if each not in content:
                        print(f'[BOOT-FATAL] Could not find variable "{each}" in boot config')
                        result = False
        except Exception as trying_boot_config_exception:
            print(f'[BOOT-FATAL] An error occurred while checking boot config: {trying_boot_config_exception}')
            result = False
    else:
        result = False
    return result   # if it returns None, it have to be some unusual situation

start = time.time()
print('[BOOT] Start booting at: ', end='')

# does boot config exists
boot = None
required_variables = ['kern_version', 'kern_main', 'shells', 'auto_choose', 'auto_shell_start', 'pre_load_exec']

if os.path.isfile('cfg/boot'):
    try:
        with open('cfg/boot') as boot_conf:
            content = json.load(boot_conf)[0]
            for each in required_variables:
                if each not in content:
                    print(f'[BOOT-FATAL] Could not find variable "{each}" in boot config')
                    boot = False
    except Exception as trying_boot_config_exception:
        print(f'[BOOT-FATAL] An error occurred while checking boot config: {trying_boot_config_exception}')
        boot = False
else:
    print('[BOOT-ERROR] Boot config does not exists!')
    files = os.listdir('./system')
    if 'kernel.py' in files and 'shell.py' in files:
        print('[BOOT] Creating new boot config...')
        try:
            default_values = [{'kern_version': 'UNKNOWN', 'kern_main': 'system/kernel.py', 'shells': [['system/shell.py',
                                                                                                       {'name': 'Default proprietary tOS shell',
                                                                                                        'version': 'UNKNOWN'}]],
                               'auto_choose': False,
                               'auto_shell_start': False, 'pre_load_exec': None}]
            with open('cfg/boot', 'w') as new_conf:
                json.dump(default_values, new_conf)
            print('[BOOT] New boot config created successfully')
        except Exception as creating_boot_config_exception:
            print(f'[BOOT-FATAL] Boot config writing failed: {creating_boot_config_exception}. Closing bootloader...')



print('[BOOT]')
