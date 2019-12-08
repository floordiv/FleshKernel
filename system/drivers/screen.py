import sys

sys.path.insert(0, '../modules')
import cfg

# from ..modules.config import get_var


driver_type = 'screen-driver'
driver_system_name = 'default-screen-driver'
driver_name = 'Default screen driver'
driver_version = '0.0.1'
driver_author = '@floordiv'
driver_description = 'Default screen driver, proprietary software, made by kernel author, @floordiv'


class screen:
    content = []


def update_settings():
    settings = cfg.json_content('screen_driver', allow_multiple_dicts=False, from_config=True)  # backward compatibility
    return settings


def update():
    pass


def printtext(*text):
    pass


def printerr(*err):
    header = err[0]
    errcode = err[1]
    errtext = err[2]


def init():
    for each in range(3):
        pass
