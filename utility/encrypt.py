# https://libraries.io/pypi/bcrypt
import base64
import hashlib
import bcrypt
import os


def encrypt(string):
    code = str.encode(string) * int(os.getenv("CALC_PSW"))
    value = bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(code).digest()),
        bcrypt.gensalt(int(os.getenv("SALT_BC"))),
    )
    return value


def checkcrypt(string, hash):
    code = str.encode(string) * int(os.getenv("CALC_PSW"))
    value = bcrypt.checkpw(
        base64.b64encode(hashlib.sha256(code).digest()),
        hash.encode("utf-8"),
    )
    return value
