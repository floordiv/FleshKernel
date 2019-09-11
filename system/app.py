import config
import importlib.util


def run(path):
    path = '../' + path[1:] if path.startswith('/') else path
    bad_functions = config.get_var('app', 'deny_functions', 'list_of_functions').split()
    bad_libs = config.get_var('app', 'deny_modules', 'list_of_modules').split()


def analyse(path):
    path = '../' + path[1:] if path.startswith('/') else path
    pass


def exists(path):
    path = '../' + path[1:] if path.startswith('/') else path
    return importlib.util.find_spec(path)


def valid(path):
    path = '../' + path[1:] if path.startswith('/') else path
    pass

