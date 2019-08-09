import os
import json


def exists(username):
    if username + '.eud' in os.listdir('../users'):
        return True
    return False


def get_all():
    users_list = []
    for file in os.listdir('../users'):
        if file.endswith('.eud'):
            users_list.append(file)

    return users_list


def get_data(username):
    if exists(username):
        with open(f'../users/{username}.eud') as user_data:
            for info in json.load(user_data):
                return info
    return False
