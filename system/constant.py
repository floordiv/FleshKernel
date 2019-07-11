import collections


class Constant(object):
    def __setattr__(self, name, value, signature=None):
        if name in self.__dict__:
            if signature is None:
                raise TypeError('Constant can not be changed')

        if not isinstance(value, collections.Hashable):
            if isinstance(value, list):
                value = tuple(value)
            elif isinstance(value, set):
                value = frozenset(value)
            elif isinstance(value, dict):
                raise TypeError('dict can not be used as constant')
            else:
                raise ValueError('Mutable or custom type is not supported')
        self.__dict__[name] = value

    def __delattr__(self, name):
        # Deny against deleting a declared constant
        if name in self.__dict__:
            raise TypeError('Constant can not be deleted')
        raise NameError("Name '%s' is not defined" % name)
