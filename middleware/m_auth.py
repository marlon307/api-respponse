from fastapi import Header
from pydantic import BaseModel, validator
from functools import wraps

from auth.auth_jwt import valid_auth
from flask import abort, request

msgErr = {
    "msg": "Unauthorized.",
    "status": 401,
}, 401


class m_auth(BaseModel):
    authorization: str = Header(default="Bearer token")

    @validator("authorization")
    def valid_auth_token(cls, v):
        print(v, 22222)
        pass


# def m_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         try:
#             if valid_auth() is not None:
#                 abort(401)

#         except Exception as err:
#             print(f"[AUTH] %s" % (err))
#             return msgErr

#         return f(*args, **kwargs)

#     return decorated


def m_auth_adm(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if valid_auth() is not None or "admin" not in request.headers["user"]:
                abort(401)
        except Exception as err:
            print(f"[AUTH] %s" % (err))
            return msgErr

        return f(*args, **kwargs)

    return decorated
