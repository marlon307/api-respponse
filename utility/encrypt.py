# https://libraries.io/pypi/bcrypt
import base64
import hashlib
import bcrypt
import os
from cryptography.fernet import Fernet


def encrypt(psw: str):
    code = str.encode(psw) * int(os.getenv("CALC_PSW", 0))
    bytes = bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(code).digest()),
        bcrypt.gensalt(int(os.getenv("SALT_BC", 0))),
    )
    return bytes


def checkcrypt(psw: str, hash: str):
    code = str.encode(psw) * int(os.getenv("CALC_PSW", 0))
    bool = bcrypt.checkpw(
        base64.b64encode(hashlib.sha256(code).digest()),
        hash.encode("utf-8"),
    )
    return bool


def fernetEncrypt(key: bytes, info_for_crypt) -> dict:
    cyper = Fernet(key)
    crypt_hash = cyper.encrypt(str(info_for_crypt).encode("utf-8"))
    return {
        "key": key,
        "crypt_hash": crypt_hash.decode("utf-8"),
    }


def fernetDecrypt(key: str, info_for_decrypt) -> str | bool:
    try:
        cyper = Fernet(str(key).encode("utf-8"))
        decrypt = cyper.decrypt(str(info_for_decrypt).encode("utf-8"))
        object_decrypt = decrypt.decode("utf-8")
        return object_decrypt
    except:
        return False
