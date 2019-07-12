class global_settings:
    pass


class log:
    files = {
         'error':       ['../log/errors'],
         'err':         ['../log/logins'],
         'bad_auth':    ['../log/bad_logins', '../log/logins'],
         'good_auth':   ['../log/good_logins', '../log/logins'],
         'warning':     ['../log/global'],
         'info':        ['../log/global'],
         'broadcast':   ['../log/broadcast_hist'],
         'parser':      ['../log/parse_hist'],
         'memory':      ['../log/memory', '../log/global'],
         'kernel':      ['../log/global', '../log/kernel_log'],
         'fatal':       ['../log/global', '../log/kernel_log']
             }

    show_type = True
    show_time = True
    show_date = True

    auto_broadcast = False


class broadcast:
    types = {
        'error': ['white', 'red'],
        'fatal': ['white', 'red'],
        'warning': ['white', 'yellow'],
        'info': ['white', 'black'],
        'success': ['white', 'green'],
        'none': ['blue', 'black']
    }

    enable_for = ['all']

    colors = True
    autolog = False
    logging = True
    allow = True
    show_type = True
    show_time = True
    show_date = True


class co_core:
    allow_broadcast = False
    allow_kernel_checking = True    # if value is False, it can proof your security

    allow_threads = True
    max_threads = 10


class memory:
    max_size = 100
    autoremove = True
    autoremove_mode = 'from-end'
    constant = True
    logging = True
    vip_cells = ['kernel', 'shell']


class kernel:
    class injections:
        allow = False
        action = ''
        control_transfer = ''

    modules = {'log': 'log',  # modules binds (you can add your own)
               'func': 'func',
               'memory': 'memory',
               'encryption': 'encryption',
               'line_parser': 'line_parser',
               'user': 'user',
               'text': 'text',
               'net': None
               }

    allow_functions_rebinding = False

    updates = False     # it can proof user's security by adding alien modules

    config = {}
