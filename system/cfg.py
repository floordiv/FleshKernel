import json
import kernel


def json_content(file, caller, allow_multiple_dicts=False, from_config=True):
    try:
        if from_config:
            file = '../cfg/' + file
        with open(file, 'r') as json_file:
            if not allow_multiple_dicts:
                return json.load(json_file)[0]
            else:
                return json.load(json_file)
    except FileNotFoundError:
        return None
