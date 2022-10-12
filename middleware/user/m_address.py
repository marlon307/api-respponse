from functools import wraps
from flask import request

msgErr = {
    "detail": "Dados enviados inválidos.",
    "status": 400,
}, 400


def m_address(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if (
                "name_delivery" not in data
                or "city" not in data
                or "district" not in data
                or "uf" not in data
                or "cep" not in data
                or "road" not in data
                or "number_home" not in data
            ):
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware address] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated
