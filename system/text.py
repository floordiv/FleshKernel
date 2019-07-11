import settings
import log


def init_modules():
    if settings.broadcast.color_output is True:
        try:
            from colorama import Fore, Style, init, deinit, reinit
            from termcolor import colored
            init()
        except Exception as import_color_output_modules_exception:
            print(f'[ERROR] Can\'t initialize colored output: {import_color_output_modules_exception}')
            log.write('error')


def output(text, fg_color='white', bg_color='black'):
    if bg_color == 'black':
        print(colored(text, fg_color))
    else:
        print(colored(text, fg_color, 'on_' + bg_color))


def stop():
    deinit()
