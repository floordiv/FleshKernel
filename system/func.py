import socket


class current:
    @staticmethod
    def time():
        import datetime
        try:
            return str(datetime.datetime.today()).split('.')[0].split()[1]
        except:
            return None

    @staticmethod
    def date():
        import datetime
        try:
            return str(datetime.datetime.today()).split('.')[0].split()[0]
        except:
            return None


class useful:
    @staticmethod
    def compare_lists(dict1, dict2):
        return {**dict1, **dict2}

    @staticmethod
    def dict_from_list(lst):
        if not len(lst) % 2 == 0:   # if the length of the list is not even
            return False

    @staticmethod
    def elements_equal_to(elements, object_to_equal):
        answer = True
        for element in elements:
            if type(element) != object_to_equal:
                answer = False

        return answer

    @staticmethod
    def dict_to_line(element):
        pass


class specific:
    @staticmethod
    def module_sockets_valid(line, modules):
        if type(line) != dict:
            return False
        if len(line) != len(modules):
            return False
        if len(line.keys()) != len(line.values()):
            return False
        if not useful.elements_equal_to(list(line.values()), int) or not useful.elements_equal_to(list(line.keys()), str):
            return False

