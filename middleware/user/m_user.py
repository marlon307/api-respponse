from functools import wraps
from flask import request
from utility.credentials import valid_email, valid_psw, valid_name

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


def m_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if data["email"] is None or valid_email(data["email"]) is not True:
                return msgErr

            if data["password"] is None or valid_psw(data["password"]) is not True:
                return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Login] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated


def m_register(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                data["name"] is None
                or len(data["name"]) < 4
                or valid_name(data["name"]) is not True
            ):
                return msgErr
            if data["email"] is None or valid_email(data["email"]) is not True:
                return msgErr

            if data["password"] is None or valid_psw(data["password"]) is not True:
                return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Register User] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated


def m_email(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if data["email"] is None or valid_email(data["email"]) is not True:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Login] ( %s )" % (err))
            return msgErr

    return decorated


def m_psw(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if data["password"] is None or valid_psw(data["password"]) is not True:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Login] ( %s )" % (err))
            return msgErr

    return decorated
