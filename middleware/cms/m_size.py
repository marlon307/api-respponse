from functools import wraps
from flask import request

msgErr = {
    "msg": "Não foi possivel inserir este tamanho.",
    "status": 400,
}, 400


def m_add_size(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if data["value_size"] is None:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add size] ( %s )" % (err))
            return msgErr

    return decorated
