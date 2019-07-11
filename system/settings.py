class global_settings:
    pass


class log:
    files = {'error':       ['../log/errors'],
             'err':         ['../log/logins'],
             'bad_auth':    ['../log/bad_logins', '../log/logins'],
             'good_auth':   ['../log/good_logins', '../log/logins'],
             'warning':     ['../log/global'],
             'info':        ['../log/global'],
             'broadcast':   ['../log/output'],
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
    color_output = True
    autolog = False
    allow = True
    show_type = True
    show_time = True
    show_date = False


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
