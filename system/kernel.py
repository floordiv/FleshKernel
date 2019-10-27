import os
import app
import config
import encryption
import memory
import func
import file_system
import line_parser
import log
import user
import socket
import errno


# default sockets for kernel modules starts with 12076


class application:

    try:
        default_modules_sockets = dict(config.get('kernel', 'default_socket_values', '*'))
        print(f'[INFO] Successfully ')
    except Exception as getting_kernel_modules_sockets_values_exception:
        print(f'[ERROR] Could not find default values for kernel modules sockets ({getting_kernel_modules_sockets_values_exception}). '
              'Setting to default (look in log)')
        kernel_modules = ['app', 'memory', 'log', 'co_core', 'file_system', 'config']
        log.write('kern_log', 'error', 'Could not find default values for kernel modules sockets ('
                                       f'{getting_kernel_modules_sockets_values_exception}). Setting to default ({[x + 12076 for x in range(len(kernel_modules))]})')
        default_modules_sockets = dict(zip(kernel_modules, [x + 12076 for x in range(len(kernel_modules))]))


def init():
    # TODO: каждый модуль будет работать на определенном сокете
    kernel_modules = ['app', 'memory', 'log', 'co_core', 'file_system', 'config']
    sockets_ok = True
    try:
        modules_sockets = dict(config.get('kernel', 'socket_values', '*'))
        print(f'[INFO] Successfully got sockets for modules. Validating...')
        log.write('kern_log', 'info', f'Successfully got sockets for modules. Validating...')
        if not func.specific.module_sockets_valid(modules_sockets):
            print('[ERROR] Config is bad or corrupted (bad data). Setting to default')
            log.write('kern_log', 'error', 'Config is bad or corrupted (bad data). Setting to default')
            raise Exception
    except Exception as getting_kernel_modules_sockets_values_exception:
        if not config.exists('kernel'):
            print('[ERROR] An error occurred because config file (config/modules) was not found')
        modules_sockets = dict(zip(kernel_modules, [x + 12076 for x in range(len(kernel_modules))]))
        print(f'[ERROR] Could not find default values for kernel modules sockets ({getting_kernel_modules_sockets_values_exception}). '
              'Setting to default (look in log)')
        log.write('kern_log', 'error', 'Could not find default values for kernel modules sockets ('
                                       f'{getting_kernel_modules_sockets_values_exception}). Setting to default ({modules_sockets})')

    last_socket = modules_sockets[list(modules_sockets)[-1]]
    modules = {}

    # it's time to check, does sockets free
    while not sockets_ok:
        errors = []

        for element in modules_sockets:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                print(f'Port {modules_sockets[element]}: ', end='')
                sock.bind(('localhost', modules_sockets[element]))
                print('ok')
                modules[element] = modules_sockets[element]
            except socket.error as opening_sockets_exception:
                if opening_sockets_exception.errno == errno.EADDRINUSE:
                    errors.append(element)
                    print('occupied')
                else:
                    print('error')
                    print(f'[FATAL] Kernel could not start: error in port {modules_sockets[element]} for module "{modules_sockets}"')
                    log.write('kern_log', 'fatal', f'An error occurred while testing port {modules_sockets[element]} for {element}:'
                                                   f' {opening_sockets_exception}')

        if len(errors) > 0:
            for error in errors:
                modules_sockets[error] = last_socket + 1
                last_socket += 1
        else:
            config.edit('kernel', 'socket_values')
            sockets_ok = True

    print('[INFO] Sockets has been initialized successfully. Initializing modules...')
    for element in modules:
        pass


init()


# very very bad person, and python hater: telegram - @barmatographOS. FUck you, idiot, py one love!
