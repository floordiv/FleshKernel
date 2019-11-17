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
            print(f'[BOOT-ERROR] An error occurred while checking boot config: {trying_boot_config_exception}')
            result = False
    else:
        result = False
    return result  # if it returns None, it have to be some unusual situation


def read_config():
    try:
        with open('./cfg/boot') as boot_conf:
            return json.load(boot_conf)[0]
    except Exception as reading_boot_config_exception:
        print(f'[BOOT-FATAL] Reading boot config failed: {reading_boot_config_exception}. Aborting...')
        os.abort()


def fix_boot_config():
    files = os.listdir('./system')
    if 'kernel.py' in files and 'shell' in os.listdir('./system'):
        print('[BOOT] Creating new boot config...')
        try:
            default_values = [{'kern_version': 'UNKNOWN', 'kern_main': 'system/kernel.py', 'filesystem_folders': ['cfg', 'system',
                                                                                                                  'system/drivers',
                                                                                                                  'system/modules'],
                               'filesystem_files': ['system/drivers/keyboard.py', 'system/drivers/screen.py', 'system/modules'],
                               'shells': [['system/shell.py',
                                           {'name': 'Default proprietary tOS shell',
                                            'version': 'UNKNOWN'}]],
                               'auto_choose': False,
                               'auto_shell_start': False, 'pre_load_exec': None}]
            try:
                with open('cfg/boot', 'w') as new_conf:
                    json.dump(default_values, new_conf)
            except Exception as creating_boot_config_exception:
                print(f'[BOOT-FATAL] Creating boot config failed: {creating_boot_config_exception}')
            print('[BOOT] New boot config created successfully')
        except Exception as creating_boot_config_exception:
            print(f'[BOOT-FATAL] Boot config writing failed: {creating_boot_config_exception}. Aborting...')
            os.abort()
    else:
        print('[BOOT-FATAL] Kernel or folder "/root/system/shell" not found! Aborting...')
        os.abort()


start = time.time()
print('[BOOT] Start booting at: ', end='')

# does boot config exists
required_variables = ['kern_version', 'kern_main', 'shells', 'filesystem_folders', 'filesystem_files', 'auto_choose', 'auto_shell_start',
                      'pre_load_exec']

boot = check_config()
if not boot:
    print('[BOOT-ERROR] Boot config does not exists!')
    fix_boot_config()

# do not look here
boot = check_config()
if not boot:
    print('[BOOT-FATAL] Boot failed because of invalid boot config. Aborting...')
    os.abort()
# and now, you can look

settings = read_config()
print(f'[BOOT-EXEC] Execute code before kernel: {settings["pre_load_exec"] is not None}')
if settings["pre_load_exec"] is not None:
    print(f'[BOOT-EXEC] Executing: {settings["pre_load_exec"]}')
    try:
        eval(f'exec("{settings["pre_load_exec"]}")')
    except Exception as executing_code_exception:
        print(f'[BOOT-EXEC] Code execution failed: {executing_code_exception}')


# start filesystem validation
required_folders = settings['filesystem_folders']
required_files = settings['filesystem_files']

finish = time.time()
print(f'[BOOT] Booting completed in: {finish - start} sec')
# run kernel init here
