from functools import wraps
from auth.auth_jwt import valid_auth
from flask import abort

msgErr = {
    "msg": "Unauthorized.",
    "status": 401,
}, 401

msgSucss = {
    "msg": "Authorization.",
    "status": 200,
}, 200


def m_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if valid_auth() is not None:
                abort(401)

        except Exception as err:
            print(f"[AUTH] %s" % (err))
            return msgErr

        return f(*args, **kwargs)

    return decorated
