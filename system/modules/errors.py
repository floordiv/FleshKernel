class Error(Exception):
    pass


class DeinitError(Error):
    def __init__(self, message):
        # self.expression = expression
        self.message = message


class DirectoryExistsError(Error):
    def __init__(self, message, directory):
        self.message = message
        self.directory = directory


class DirectoryDoesntExistsError(Error):
    def __init__(self, message, directory):
        self.message = message
        self.directory = directory


class AccessDenied(Error):
    def __init__(self, message):
        self.message = message
