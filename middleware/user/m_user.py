from functools import wraps
from flask import request
from utility.credentials import valid_email, valid_psw, valid_name
from utility.format_doc import format_cpf
from utility.valid_cpf import cpf_validate

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


def m_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()

            if (
                "email" not in data
                or data["email"] is None
                or valid_email(data["email"]) is not True
            ):
                return msgErr

            if (
                "password" not in data
                or data["password"] is None
                or valid_psw(data["password"]) is not True
            ):
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
                "name" not in data
                or data["name"] is None
                or len(data["name"]) < 4
                or valid_name(data["name"]) is not True
            ):
                return msgErr
            if (
                "email" not in data
                or data["email"] is None
                or valid_email(data["email"]) is not True
            ):
                return msgErr

            if (
                "password" not in data
                or data["password"] is None
                or valid_psw(data["password"]) is not True
            ):
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
            if (
                "email" not in data
                or data["email"] is None
                or valid_email(data["email"]) is not True
            ):
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
            if (
                "password" not in data
                or data["password"] is None
                or valid_psw(data["password"]) is not True
            ):
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware Login] ( %s )" % (err))
            return msgErr

    return decorated


def m_update_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            list_key_onj = ["cel", "date", "doc", "gender", "name", "tel"]
            data = request.get_json()

            for key in data:
                if key not in list_key_onj:
                    return msgErr

            if (
                valid_name(data["name"]) is not True
                or cpf_validate(data["doc"]) is False
            ):
                return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware update_user] ( %s )" % (err))
            return msgErr

    return decorated
