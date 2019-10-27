import log
import collections


class const(object):

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
                raise TypeError('Dict can\'t be used as constant!')
            else:
                raise TypeError('Mutable or custom type can\'t be used as constant!')
        self.__dict__[name] = value
        return 'constant-successfully-added'

    def __delattr__(self, name):
        # Deny against deleting a declared constant
        if name in self.__dict__:
            raise MemoryError('Constant can\'t be deleted!')
        raise NameError("Variable not found!" % name)


class vars:
    __memory = {}
    __recent_calls = ()
    __cellmodes = {}
    __varmodes = {}         # modes: w, r, a

    def write(self, key, value, name='global', mode='w'):
        if name in vars.__memory and key in vars.__memory[name]:    # does given cell exists
            log.write('memory', f'Request to rewrite variable "{key}" from "{name}"')
            pass
        else:
            log.write('memory', f'Request to create new variable "{key}" from "{name}"')
            vars.__memory[name] = {}

        # TODO: add mode check
        vars.__memory[name][key] = value
        log.write('memory', 'Request completed successfully')

    def read(self, key, name='global'):
        pass

    def remove(self, key, name='global'):
        pass


def write(key, value, name='global', mode='w'):
    vars.write(0, key, value, name=name, mode=mode)


def read(key, name='global'):
    vars.read(0, key, name=name)


def remove(key, name='global'):
    vars.remove(0, key, name=name)


const.my_tuple = (('a', 'hello'), ('world', 'me'))
# print(const.my_tuple)
a = const.my_tuple
print(type(a))
print('hello')
