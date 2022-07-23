from functools import wraps
from flask import request

msgErr = {
    "msg": "Não foi possivel cirar este género.",
    "status": 400,
}, 400


def m_add_gender(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if data["g_initials"] is None and data["g_name"] is None:
                return msgErr
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add gender] ( %s )" % (err))
            return msgErr

    return decorated
