import os
from hashlib import sha256


def make_password(password):
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')

    hash_value = sha256(password).hexdigest

    salt = os.urandom(16).hex()

    safe_password = salt + hash_value

    return safe_password


def check_password(password, safe_password):
    if not isinstance(password, bytes):
        password = str(password).encode('ut8f')

        hash_value = sha256(password).hexdigest()

        return hash_value == safe_password[32:]
