from functools import wraps
from flask import request, abort

msgErr = {
    "msg": "Não foi possivel cirar este género.",
    "status": 400,
}, 400


def m_add_gender(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            data = request.get_json()
            if "g_initials" not in data or "g_name" not in data:
                abort(400, msgErr)
            return f(*args, **kwargs)

        except Exception as err:
            print(f"[Middleware add gender] ( %s )" % (err))
            abort(400, msgErr)

    return decorated
