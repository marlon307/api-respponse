from functools import wraps
from auth.auth_jwt import valid_auth
from flask import abort, request

msgErr = {
    "msg": "Unauthorized.",
    "status": 401,
}


def m_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if valid_auth() is not None:
                abort(401)

        except Exception as err:
            print(f"[AUTH] %s" % (err))
            abort(401, msgErr)

        return f(*args, **kwargs)

    return decorated


def m_auth_adm(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if valid_auth() is not None or "admin" not in request.headers["user"]:
                abort(401)
        except Exception as err:
            print(f"[AUTH] %s" % (err))
            abort(401, msgErr)

        return f(*args, **kwargs)

    return decorated
