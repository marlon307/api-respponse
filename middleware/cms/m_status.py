from functools import wraps
from flask import request

msgErr = {
    "msg": "Não foi possivel inserir este status.",
    "status": 400,
}, 400


def m_add_status(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if "s_name" not in data:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add status] ( %s )" % (err))
            return msgErr

    return decorated
