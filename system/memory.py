import log
import settings


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
