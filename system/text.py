# import settings
# import log
from termcolor import colored


def output(text, fg_color='white', bg_color='black', end='\n'):
    # if settings.broadcast.colors:
    if True:
        if bg_color == 'black':
            print(colored(text, fg_color), end=end)
        else:
            print(colored(text, fg_color, 'on_' + bg_color), end=end)
    else:
        print(text)
