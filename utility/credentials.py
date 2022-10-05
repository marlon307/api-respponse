import re
import os


def valid_name(name: str):
    if re.fullmatch(r"%s" % os.getenv("VALID_NAME"), name):
        return True
    return False


def valid_email(email: str) -> bool:
    print(os.getenv("VALID_EMAIL"), email)
    if re.fullmatch(r"%s" % os.getenv("VALID_EMAIL"), email):
        return True
    return False


def valid_psw(psw: str) -> bool:
    if re.fullmatch(r"%s" % os.getenv("VALID_PSW"), psw):
        return True
    return False
