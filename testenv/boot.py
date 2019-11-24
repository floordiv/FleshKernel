import time
import os
import json
import datetime
import importlib
import traceback

start = time.time()
start_time = datetime.datetime.now()


def check_config():
    result = True
    if os.path.isfile('cfg/boot'):
        try:
            with open('cfg/boot') as boot_conf:
                content = json.load(boot_conf)[0]
                for each in required_variables:
                    if each not in content:
                        print(f'[BOOT-FATAL] Could not find variable "{each}" in boot config')
                        log(f'[FATAL] Could not find variable "{each}" in boot config')
                        result = False
        except Exception as trying_boot_config_exception:
            print(f'[BOOT-ERROR] An error occurred while checking boot config: {trying_boot_config_exception}')
            log(f'[ERROR] An error occurred while checking boot config: {trying_boot_config_exception}')
            result = False
    else:
        result = False
    return result  # if it returns None, it have to be some unusual situation


def log(text):
    if 'log' not in os.listdir('.'):
        os.mkdir('log')
    if 'boot' not in os.listdir('./log'):
        open('./log/boot', 'w').close()     # create log file
    with open('./log/boot', 'a') as log_file:
        log_file.write(f'[{datetime.datetime.now()}] {text}\n')


def check_filesystem():
    req_folders = ['system', 'system/shell']
    boot_greenlight = True
    for each in req_folders:
        if not os.path.exists(each):
            print(f'[BOOT-FATAL] Required folder not found: {each}')
            boot_greenlight = False
            log(f'[FATAL] Required folder not found: {each}')
    return boot_greenlight


def read_config():
    try:
        with open('./cfg/boot') as boot_conf:
            return json.load(boot_conf)[0]
    except Exception as reading_boot_config_exception:
        print(f'[BOOT-FATAL] Reading boot config failed: {reading_boot_config_exception}. Aborting...')
        log(f'[FATAL] Reading boot config failed: {reading_boot_config_exception}. Aborting...')
        os.abort()


def find_inf():
    files = os.listdir('./system/shell')
    inf_files = []
    result = {}
    print('[BOOT] Looking for *.inf files in /root/system/shell...')
    log('Looking for *.inf files in /root/system/shell...')
    for file in files:
        if file.endswith('.inf'):
            file = ".".join(file.split(".")[:-1])
            print(f'[BOOT] *.inf file found: {file}')
            log(f'*.inf file found: {file}')
            inf_files.append(file)

    for each in inf_files:
        print(f'[BOOT] Reading .inf file: {each}.inf')
        log(f'Reading .inf file: {each}.inf')
        with open(f'./system/shell/{each}.inf', 'r') as content:
            content = content.read().split('\n')
        result[each] = {}
        for element in content:
            result[each][element.split(':')[0]] = element.split(':')
        print(f'[BOOT] {each}.inf: variables: {", ".join(list(result[each].keys()))}')
        log(f'{each}.inf: variables: {", ".join(list(result[each].keys()))}')
    return result


def valid_infs(result, required_vars=('name', 'main')):
    for var in required_vars:
        if var not in result:
            return False
    return True


def valid_inf(infname, infval, required_vars=('name', 'main')):
    for each in required_vars:
        if each not in infval:
            return infname
    return True


def fix_boot_config(abort_without_shell=True):
    files = os.listdir('./system')
    result = find_inf()
    invalid_inf = []
    if not valid_infs(result):
        for each in result:
            if not valid_inf(each, result[each]):
                invalid_inf.append(each)
    if len(invalid_inf) > 0:
        for each in invalid_inf:
            del result[each]
    if len(list(result.keys())) == 0:
        print(f'[BOOT-FATAL] Boot config recovery failed: no shells for kernel found')
        log(f'[FATAL] Boot config recovery failed: no shells for kernel found')
        if abort_without_shell:
            print('[BOOT] Aborting...')
            log('Aborting...')
            os.abort()
        print('[BOOT] Aborting cancelled')
        log('Aborting cancelled')
    if 'kernel.py' in files and len(result) > 0:
        print('[BOOT] Creating new boot config...')
        log('Creating new boot config...')
        try:
            shells = []
            try:
                for elem in result:
                    temp = [elem, result[elem]]
                    shells.append(temp)
            except Exception as listing_shells_exception:
                print(f'[BOOT-ERROR] Shell listing failed: {listing_shells_exception}')
                log(f'[ERROR] Shell listing failed: {listing_shells_exception}')
                shells = [None]
            default_values = [{'kern_version': 'UNKNOWN', 'kern_main': 'system/kernel.py', 'shells': shells, 'auto_choose': False,
                               'pre_load_exec': None}]
            try:
                root_files = os.listdir('.')
                if 'cfg' not in root_files:
                    os.mkdir('cfg')
                with open('./cfg/boot', 'w') as new_conf:
                    json.dump(default_values, new_conf)
            except Exception as creating_boot_config_exception:
                print(f'[BOOT-FATAL] Creating boot config failed: {creating_boot_config_exception}. Aborting...')
                log(f'[FATAL] Creating boot config failed: {creating_boot_config_exception}. Aborting...')
                os.abort()
            print('[BOOT] New boot config created successfully')
            log('New boot config created successfully')
        except Exception as creating_boot_config_exception:
            print(f'[BOOT-FATAL] Boot config writing failed: {creating_boot_config_exception}. Aborting...')
            log(f'[FATAL] Boot config writing failed: {creating_boot_config_exception}. Aborting...')
            os.abort()
    else:
        print('[BOOT-FATAL] Kernel or shell not found! Aborting...')
        log('[FATAL] Kernel or shell not found! Aborting...')
        os.abort()


print(f'[BOOT] Start booting at: {start_time}')
log(f'Booting...')
print('[BOOT] Checking required folders...')
log('Checking required folders...')
filesystem_ok = check_filesystem()
if not filesystem_ok:
    print('[BOOT-FATAL] Aborting...')
    log('[FATAL] Some of the folders does not exist. Aborting...')
    os.abort()

# does boot config exists
required_variables = ['kern_version', 'kern_main', 'shells', 'auto_choose', 'pre_load_exec']

boot = check_config()
if not boot:
    print('[BOOT-ERROR] Boot config does not exists! Trying to fix it...')
    log('[ERROR] Boot config does not exists! Trying to fix it...')
    fix_boot_config()

# do not look here
boot = check_config()
if not boot:
    print('[BOOT-FATAL] Boot failed because of invalid boot config. Aborting...')
    log('[FATAL] Boot failed because of invalid boot config. Aborting...')
    os.abort()
# now you can

settings = read_config()
print(f'[BOOT-EXEC] Execute code before kernel: {settings["pre_load_exec"] is not None}')
log(f'[EXEC] Execute code before kernel: {settings["pre_load_exec"] is not None}')
if settings["pre_load_exec"] is not None:
    print(f'[BOOT-EXEC] Executing: {settings["pre_load_exec"]}')
    log(f'[EXEC] Executing: {settings["pre_load_exec"]}')
    try:
        eval(f'exec("{settings["pre_load_exec"]}")')
    except Exception as executing_code_exception:
        print(f'[BOOT-EXEC] Code execution failed: {executing_code_exception}')
        log(f'[EXEC] Code execution failed: {executing_code_exception}')

finish = time.time()
print(f'[BOOT] All main boot functions has ran successfully at: {datetime.datetime.now()}')
log(f'All main boot functions has ran successfully at: {datetime.datetime.now()}')
print(f'[BOOT] Booting completed in: {finish - start} sec. Initializing kernel...')
log(f'Booting completed in: {finish - start} sec. Initializing kernel...')
# run kernel init here
try:
    kernel = importlib.import_module(f'./{".".join(settings["kern_main"].split(".")[:-1])}')
    kernel.init()
except Exception as initializing_kernel_exception:
    print(f'[BOOT-FATAL] Kernel initializing failed: {initializing_kernel_exception}. More info:\n\n{traceback.format_exc()}')
    log(f'[FATAL] Kernel initializing failed: {initializing_kernel_exception}. More info:\n{traceback.format_exc()}')
