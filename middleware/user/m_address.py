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
            data = request.get_json()
            if (
                data["name_delivery"] is None
                and data["city"] is None
                and data["district"] is None
                and data["uf"] is None
                and data["cep"] is None
                and data["road"] is None
                and data["number_home"] is None
            ):
                return msgErr

            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware address] ( %s ) [%s]" % ("data", err))
            return msgErr

    return decorated
