# import config
# print(config.new('app', {'deny_functions': {'list_of_functions': 'print input open'}, 'deny_modules': {'list_of_modules': 'os sys builtins'}}))

import importlib.util
module_spec = importlib.util.find_spec('test2')
module = importlib.util.module_from_spec(
    importlib.util.find_spec('test2'))


def printer():
    print('I\'m here!')


module.__dict__['printer'] = printer
module.__dict__['lol'] = 'nonono test'
print(vars(module))
# print(module.__dict__)
importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
