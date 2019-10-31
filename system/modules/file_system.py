import os
import shutil

a = 'test'


class file:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def edit(path, data):
        if file.isfile(path):
            path = path[1:] if path.startswith('/') else path
            with open(f'../{path}', 'r') as file_for_edit:
                lines = file_for_edit.readlines()
            for line in data:
                if 'int' not in str(type(line)):
                    continue
                lines[line] = data[line]
            with open(f'../{path}', 'w') as final_file:
                final_file.write('\n'.join(lines))

    @staticmethod
    def write(path, text, mode='a'):
        modes = ['a', 'w']
        if mode not in modes:
            raise Exception('bad file write mode')
        path = path[1:] if path.startswith('/') else path
        if file.isfile(path):
            with open(f'../{path}', mode) as user_file:
                user_file.write(text)
        return 'success'

    @staticmethod
    def read(path):
        if file.isfile(path):
            path = path[1:] if path.startswith('/') else path
            return open(f'../{path}', 'r').read()
        return FileNotFoundError('bad path to file!')

    @staticmethod
    def create(path):
        # if file.is_file(0, path):         I don't need this code anymore, because explored a new file mode, x
        #     raise FileExistsError(f'file exists!')
        path = path[1:] if path.startswith('/') else path
        open(f'../{path}', 'x')
        return 'success'

    @staticmethod
    def exists(path):
        path = path[1:] if path.startswith('/') else path
        return os.path.exists(f'../{path}')

    @staticmethod
    def isfile(path):
        path = path[1:] if path.startswith('/') else path
        return os.path.isfile(f'../{path}')


class direction:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def create(self, path):
        path = '../' + path[1:] if path.startswith('/') else path
        if direction.exists(path):
            raise IsADirectoryError('path exists!')
        try:
            os.mkdir(path)
            return 'success'
        except Exception as creating_direction_exception:
            return str(creating_direction_exception)

    @staticmethod
    def content(path):
        path = '../' + path[1:] if path.startswith('/') else path
        return os.listdir(path)

    @staticmethod
    def recursion_content(path):
        path = '../' + path[1:] if path.startswith('/') else path

        content = []

        for element in os.walk(path):
            content.append(element)

        return content

    @staticmethod
    def remove(path):
        path = '../' + path[1:] if path.startswith('/') else path
        if direction.exists(path):
            try:
                os.rmdir(path)
                return 'success'
            except Exception as removing_direction_exception:
                return str(removing_direction_exception)

    @staticmethod
    def move(path, new_path):
        path = '../' + path[1:] if path.startswith('/') else path
        new_path = '../' + path[1:] if path.startswith('/') else path

        try:
            shutil.move(path, new_path)
        except Exception as moving_directory_exception:
            return str(moving_directory_exception)

    @staticmethod
    def rename(path, new_dir_name):
        path = '../' + path[1:] if path.startswith('/') else path
        new_dir_name = f'../{"/".join(path.split("/")[1:-1])}/{new_dir_name}'
        if direction.exists(path):
            if not file.isfile(path):
                os.rename(path, new_dir_name)
                return 'success'
        return NotADirectoryError('invalid path!')

    @staticmethod
    def isdir(path):
        path = '../' + path[1:] if path.startswith('/') else path
        return os.path.isdir(path)

    @staticmethod
    def exists(path):
        path = '../' + path[1:] if path.startswith('/') else path
        return os.path.exists(path)
