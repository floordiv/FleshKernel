import json

data = {'new_boot_data': []}

data['new_boot_data'].append({'kern_version': '0.0.1', 'kern_main': 'system/kernel.py', 'shells': [['system/shell.py', {'name': 'Default proprietary tOS shell', 'version': '0.0.1'}]], 'auto_choose': False,
                              'auto_shell_start': False, 'pre_load_exec': None})

with open('cfg/boot', 'w') as json_file:
    json.dump(data['new_boot_data'], json_file)
