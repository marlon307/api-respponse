import re


def valid_name(name):
    if re.fullmatch(
        r"^([a-zA-Z]{3,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)", name
    ):
        return True
    return False


def valid_email(email):
    if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return True
    return False


def valid_psw(psw):
    if re.fullmatch(r"(^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,})", psw):
        return True
    return False
