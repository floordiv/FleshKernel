import configparser
import os


class var:
    types = {
        'dict': dict,
        'str': str,
        'list': list,
        'tuple': tuple,
        'int': int,
        'float': float
    }


"""
options = {'section1': {'var': 'test'}}
"""


def new(name, options, return_info=False):
    try:
        if return_info:
            return 'This function makes new config. If a config with such name exists, it will be rewritten'
        config = configparser.ConfigParser()

        # and now, we should get all the required sections
        sections = []
        for section in options:         # get all the sections
            sections.append(section)

        # create all the required sections
        for sector in sections:
            config.add_section(sector)

        # it's time to add all the data into the sections
        for element in sections:            # each section
            for variable in options[element]:   # each variable in variables of section
                config.set(element, variable, options[element][variable])

        with open(f'../cfg/{name}', 'w') as config_file:
            config.write(config_file)
        return 'success'
    except Exception as writing_new_config_exception:
        return str(writing_new_config_exception)


def exists(name):
    return os.path.isfile(f'../config/{name}')


def edit(name, new_options):
    try:
        config = configparser.ConfigParser()
        config.read(f'../config/{name}')
        for sector in new_options:
            for variable in new_options[sector]:
                config.set(sector, variable, new_options[sector][variable])

        with open(f'../config/{name}', 'w') as config_file:
            config.write(config_file)

        return 'new-options-saved-successfully'
    except Exception as saving_new_options_exception:
        return str(saving_new_options_exception)


def var_to_var_with_type(value, mode='from_text'):
    if mode == 'from_text':
        if not value.strip().startswith('type:'):
            return False
        value = value.strip().split('|')
        value_type = value[0].split(':')[1]
        value = value[1]
        if value_type not in var.types:
            return False
        if value_type == 'dict':
            values = value.split('.')
            dict_to_return = {}
            for element in values:
                values_in_current_element = element.split(':')[1].split(',')
                dict_to_return[element.split(':')[0]] = values_in_current_element

            return dict_to_return
        elif value_type in ['int', 'float']:
            list_with_number_to_return = []
            for element in value.split(','):
                try:
                    list_with_number_to_return.append(var.types[element])
                except TypeError:
                    pass

            return list_with_number_to_return
        else:
            return var.types[value.split(',')]
    elif mode == 'from_type':
        if type(value) == dict:
            pass


def get_var(name, section, variable):
    config = configparser.ConfigParser()
    config.read(f'../config/{name}')
    data_to_return = []
    if section == '*':
        for sector in config.sections():
            try:
                data_to_return.append(config.get(sector, variable))
            except:
                pass
        return data_to_return
    elif variable == '*':
        return config.items(section)

    value = config.get(section, variable)
    value_has_type = var_to_var_with_type(value)
    return value_has_type if value_has_type is not False else value


def remove(name, options, remove_config=False):
    try:
        if remove_config:
            os.remove(f'../config/{name}')
            return f'config-{name}-removed-successfully'
        config = configparser.ConfigParser()
        config.read(f'../config/{name}')

        for section in options:
            if options[section] == '*':
                config.remove_section(section)
                continue
            for var_to_remove in options[section]:
                config.remove_option(section, var_to_remove)

        with open(f'../config/{name}', 'w') as config_file:
            config.write(config_file)
        return 'options-removed-successfully'
    except Exception as removing_config_exception:
        return str(removing_config_exception)

