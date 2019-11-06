import modules.log as log


class vars:
    __memory = {}            # modes: w, r, a, const
    __recent_calls = []

    @staticmethod
    def write(key, value, name, cell_name='global', mode='w'):
        if cell_name in vars.__memory and key in vars.__memory[cell_name]:    # does given cell exists
            log.write('memory', f'Request to rewrite variable "{key}" from "{name}" in {cell_name}')
            if vars.__memory[cell_name][key][0] == 'const':
                raise MemoryError(f'variable "{key}" from "{cell_name}" is constant!')
            elif vars.__memory[cell_name][key][0] == 'r' and name != cell_name:
                raise MemoryError(f'variable "{key}" from "{cell_name}" is read-only!')
        else:
            log.write('memory', f'Request to create new variable "{key}" from "{name}" in {cell_name} with mode "{mode}"')
            vars.__memory[cell_name] = {}

        vars.__memory[cell_name][key] = [mode, value]
        log.write('memory', f'Request to create new variable {key} from {name} in {cell_name} completed successfully')
        vars.__recent_calls.append(['new-var', name, f'{cell_name}.{key}'])

    @staticmethod
    def read(key, name, cell_name='global'):
        log.write('memory', 'read', f'reading variable {key} in {cell_name} by {name}')
        vars.__recent_calls.append(['read', name, f'{cell_name}.{key}'])
        try:
            return vars.__memory[cell_name][key][1]
        except:
            raise MemoryError(f'variable {key} in {cell_name} not found!')

    @staticmethod
    def remove(key, name, cell_name='global'):
        try:
            vars.__memory[cell_name][key][1]
        except:
            raise MemoryError(f'variable {key} in {cell_name} not found!')
        if vars.__memory[cell_name][key] != 'const' or name == cell_name:
            del vars.__memory[cell_name][key]
            log.write('memory', 'removed', f'removed variable "{key}" in "{cell_name}" by "{name}"')
            vars.__recent_calls.append(['remove', name, f'{cell_name}.{key}'])
        else:
            raise MemoryError(f'variable  "{key}" in "{cell_name}" is constant!')

    @staticmethod
    def last_actions():
        return vars.__recent_calls


def write(key, value, name, cell_name='global', mode='w'):
    return vars.write(key, value, name, cell_name=cell_name, mode=mode)


def read(key, name, cell_name='global'):
    return vars.read(key, name, cell_name=cell_name)


def remove(key, name, cell_name='global'):
    return vars.remove(key, name, cell_name=cell_name)


def last_actions():
    return vars.last_actions()

