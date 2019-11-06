import os
import shutil
import errors


class file:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def edit(path, data, from_app):
        if file.isfile(path, from_app):
            path = path[1:] if path.startswith('/') else path
            with open(f'../{path}', 'r') as file_for_edit:
                lines = file_for_edit.readlines()
            for line in data:
                if 'int' not in str(type(line)):
                    continue
                lines[line] = data[line]
            with open(f'../{path}', 'w') as final_file:
                final_file.write('\n'.join(lines))
        else:
            raise FileNotFoundError('path is wrong or file does not exists')

    @staticmethod
    def write(path, text, from_app, mode='a'):
        modes = ['a', 'w']
        if mode not in modes:
            raise Exception('bad file write mode')
        path = path[1:] if path.startswith('/') else path
        if file.isfile(path, from_app):
            with open(f'../{path}', mode) as user_file:
                user_file.write(text)
        return 'success'

    @staticmethod
    def read(path, from_app):
        if file.isfile(path, from_app):
            path = path[1:] if path.startswith('/') else path
            return open(f'../{path}', 'r').read()
        raise FileNotFoundError('path is wrong or file does not exists')

    @staticmethod
    def create(path, from_app):
        # if file.is_file(0, path):         I don't need this code anymore, because explored a new file mode, x
        #     raise FileExistsError(f'file exists!')
        path = path[1:] if path.startswith('/') else path
        open(f'../{path}', 'x')
        return 'success'

    @staticmethod
    def exists(path, from_app):
        path = path[1:] if path.startswith('/') else path
        return os.path.exists(f'../{path}')

    @staticmethod
    def isfile(path, from_app):
        path = path[1:] if path.startswith('/') else path
        return os.path.isfile(f'../{path}')


class directory:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def create(path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        if directory.exists(path, from_app):
            raise errors.DirectoryExistsError('given directory is already exists: ', path)
        try:
            os.mkdir(path)
            return 'success'
        except Exception as creating_direction_exception:
            return str(creating_direction_exception)

    @staticmethod
    def content(path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        return os.listdir(path)

    @staticmethod
    def recursion_content(path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        if not os.path.exists(path):
            raise errors.DirectoryDoesntExistsError('directory does not exists: ', path)

        content = []

        for element in os.walk(path):
            content.append(element)

        return content

    @staticmethod
    def remove(path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        if directory.exists(path, from_app):
            try:
                os.rmdir(path)
                return 'success'
            except Exception as removing_direction_exception:
                return str(removing_direction_exception)
        else:
            raise errors.DirectoryDoesntExistsError('directory does not exists: ', path)

    @staticmethod
    def move(path, new_path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        new_path = '../' + new_path[1:] if new_path.startswith('/') else path
        if not os.path.exists(path):
            raise errors.DirectoryDoesntExistsError('old directory does not exists: ', path)
        if not os.path.exists(new_path):
            os.mkdir(new_path)

        try:
            shutil.move(path, new_path)
        except Exception as moving_directory_exception:
            return str(moving_directory_exception)

    @staticmethod
    def rename(path, new_dir_name, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        new_dir_name = f'../{"/".join(path.split("/")[1:-1])}/{new_dir_name}'
        if directory.exists(path, from_app):
            if not file.isfile(path, from_app):
                os.rename(path, new_dir_name)
                return 'success'
        raise errors.DirectoryDoesntExistsError('directory does not exists: ', path)

    @staticmethod
    def isdir(path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        return os.path.isdir(path)

    @staticmethod
    def exists(path, from_app):
        path = '../' + path[1:] if path.startswith('/') else path
        return os.path.exists(path)
