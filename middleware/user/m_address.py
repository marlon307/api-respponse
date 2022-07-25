from functools import wraps
from flask import request
from utility.credentials import valid_email, valid_psw

msgErr = {
    "msg": "Credenciais Inválidas.",
    "status": 400,
}, 400


def m_address(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            # data = request.get_json()
            # if data["email"] is None or valid_email(data["email"]) is not True:
            #     return msgErr

            # if data["password"] is None or valid_psw(data["password"]) is not True:
            #     return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware address] ( %s ) [%s]" % ("data", err))
            return msgErr

    return decorated
