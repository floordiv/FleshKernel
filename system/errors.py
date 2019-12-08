class Error(Exception):
    pass


class DeinitError(Error):
    def __init__(self, message):
        self.message = message


class DirectoryExistsError(Error):
    def __init__(self, message, directory):
        self.message = message
        self.directory = directory


class DirectoryDoesNotExistsError(Error):
    def __init__(self, message, directory):
        self.message = message
        self.directory = directory


class AccessDenied(Error):
    def __init__(self, message):
        self.message = message


class KernelFatal(Error):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class DriverNotFound(Error):
    def __init__(self, message):
        self.message = message
