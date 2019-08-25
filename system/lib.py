import importlib.util


def exists(path):
    return importlib.util.find_spec(path)


def get_source(path):
    if exists(path):
        return open(path).read().strip('\n')
    return None


def get_source_lines(path):
    if exists(path):
        return open(path).readlines()
    return None


def run(path):
    if exists(path):
        source = open(path).read().strip('\n')
        source_lines = open(path).readlines()

