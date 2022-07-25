from functools import wraps
from flask import request

msgErr = {
    "msg": "Dados enviados inválidos.",
    "status": 400,
}, 400


def m_telephone(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if "n_phone" not in data:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware telephone] ( %s ) [%s]" % (data, err))
            return msgErr

    return decorated
