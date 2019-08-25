import config
bad_functions = config.get_var('app', 'deny_functions', 'list_of_functions').split()
bad_libs = config.get_var('app', 'deny_modules', 'list_of_modules').split()

