import errors
    def edit(path, data, from_app):
        if file.isfile(path, from_app):
        else:
            raise FileNotFoundError('path is wrong or file does not exists')
    def write(path, text, from_app, mode='a'):
        if file.isfile(path, from_app):
    def read(path, from_app):
        if file.isfile(path, from_app):
        raise FileNotFoundError('path is wrong or file does not exists')
    def create(path, from_app):
    def exists(path, from_app):
    def isfile(path, from_app):
class directory:
    def create(path, from_app):
        if directory.exists(path, from_app):
            raise errors.DirectoryExistsError('given directory is already exists: ', path)
    def content(path, from_app):
    def recursion_content(path, from_app):
        if not os.path.exists(path):
            raise errors.DirectoryDoesntExistsError('directory does not exists: ', path)
    def remove(path, from_app):
        if directory.exists(path, from_app):
        else:
            raise errors.DirectoryDoesntExistsError('directory does not exists: ', path)
    def move(path, new_path, from_app):
        new_path = '../' + new_path[1:] if new_path.startswith('/') else path
        if not os.path.exists(path):
            raise errors.DirectoryDoesntExistsError('old directory does not exists: ', path)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
    def rename(path, new_dir_name, from_app):
        if directory.exists(path, from_app):
            if not file.isfile(path, from_app):
        raise errors.DirectoryDoesntExistsError('directory does not exists: ', path)
    def isdir(path, from_app):
    def exists(path, from_app):