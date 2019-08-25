import configparser
import os


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

        print(os.getcwd())

        with open(f'flesh_kernel/config/{name}', 'w') as config_file:
            config.write(config_file)
        return 'success'
    except Exception as writing_new_config_exception:
        return str(writing_new_config_exception)


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


def get_var(name, section, var):
    try:
        config = configparser.ConfigParser()
        config.read(f'../config/{name}')
        data_to_return = []
        if section == '*':
            for sector in config.sections():
                try:
                    data_to_return.append(config.get(sector, var))
                except:
                    pass
            return data_to_return
        elif var == '*':
            return config.items(section)
        return config.get(section, var)
    except Exception as reading_data_from_config_exception:
        return str(reading_data_from_config_exception)


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


# new('d', {'sector1': {'var1': 'test1', 'var2': 'test2'}, 'sector2': {'var1': 'test1', 'var2': 'test2'}})
# remove('d', {'sector1': '*', 'sector2': ['var1']})
# print(get_var('d', 'sector1', 'var1'))
# print(get_var('d', 'sector1', '*'))
# print(get_var('d', 'sector2', '*'))
# edit('d', {'sector1': {'var1': 'true_test', 'var2': 'fuck this shit'}})
# print(get_var('d', 'sector1', '*'))
# print(edit('d', {'sector1': {'var50': 'rgtg'}}))
# print(get_var('d', 'sector1', '*'))




