def write(name, text, *args):
    with open(f'../log/{name}')
        line = f'{" ".join(args).upper()} {" " * 4} {text}'

