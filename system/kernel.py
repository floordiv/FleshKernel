class application:
    pass


def init():
    import settings
    global memory, log
    log = __import__(settings.kernel.modules['log'])
    memory = __import__(settings.kernel.modules['memory'])
    log.write('info', 'Starting kernel initializing')
    log.write('info', 'Logging module and settings loaded successfully')
    log.write('info', f'Loading modules: {settings.kernel.modules}')
    for _module in settings.kernel.modules:
        globals()[_module] = __import__(settings.kernel.modules[_module])

