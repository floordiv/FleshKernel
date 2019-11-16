import hashlib


def sha1(encrypting_data):
    return hashlib.sha1(encrypting_data.encode('utf-8')).hexdigest()


def sha3_224(encrypting_data):
    return hashlib.sha3_224(encrypting_data.encode('utf-8')).hexdigest()


def sha3_256(encrypting_data):
    return hashlib.sha3_256(encrypting_data.encode('utf-8')).hexdigest()


def sha3_384(encrypting_data):
    return hashlib.sha3_384(encrypting_data.encode('utf-8')).hexdigest()


def sha3_512(encrypting_data):
    return hashlib.sha3_512(encrypting_data.encode('utf-8')).hexdigest()


def sha224(encrypting_data):
    return hashlib.sha224(encrypting_data.encode('utf-8')).hexdigest()


def sha256(encrypting_data):
    return hashlib.sha256(encrypting_data.encode('utf-8')).hexdigest()


def sha384(encrypting_data):
    return hashlib.sha384(encrypting_data.encode('utf-8')).hexdigest()


def sha512(encrypting_data):
    return hashlib.sha512(encrypting_data.encode('utf-8')).hexdigest()


def shake_128(encrypting_data):
    return hashlib.shake_128(encrypting_data.encode('utf-8')).hexdigest()


def shake_256(encrypting_data):
    return hashlib.shake_256(encrypting_data.encode('utf-8')).hexdigest()

