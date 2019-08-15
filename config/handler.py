import os
memory = __import__('../system/memory')
import configparser


def exists(name):
    if name in get_all():
        return True
    else:
        return False


def get_all():
    ignore = get('handler')['']
    for file in os.listdir('.'):
        pass


def get(name):
    if exists(name):
        pass
    # value_types = {
    #     'dict': dict,
    #     'list': list,
    #     'str':  str,
    #     'int':  int,
    #                }
    #
    # if exists(name):
    #     with open(name) as config:
    #         data = config.readlines()
    #
    #     header = data[0]
    #     if header == 'list':       # if type of config is list - we should not do anything
    #         return data
    #     else:                      # but if it don't - we have to create a dictionary
    #         data_to_return = {}
    #         for element in data[1:]:
    #             element = element.strip()
    #             if element.startswith('valueType'):
    #                 value_type = element.split('|')[0].split(':')[1]
    #                 if value_type in value_types:
    #                     pass
    #                 else:
    #                     value_type = 'str'
    #             else:
    #                 value_type = 'str'
    #             line_data = element.strip().split('=')
    #             data_to_return[line_data[0]] = value_types[value_type](line_data[1])
    #         return data_to_return
    # else:
    #     return 'not-found'

