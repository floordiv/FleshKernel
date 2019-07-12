import hashlib


def encrypt(encrypting_data):
    return hashlib.sha256(encrypting_data.encode('utf-8')).hexdigest()


print(encrypt('root'))
