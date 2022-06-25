import os
import jwt
from flask import request
from datetime import datetime, timedelta

msg = {
    "msg": "Acesso não autorizado!",
    "status": 401,
}, 401


def generate_token(data):
    data["exp"] = datetime.now() + timedelta(hours=6)
    return jwt.encode(
        payload=data,
        key=os.getenv("JWT_KEY"),
        algorithm=os.getenv("ALGORITHM"),
    )


def valid_auth():
    try:
        auth = request.headers["Authorization"]
        if "Bearer" in auth:

            jwt.decode(
                jwt=auth.split(" ")[1],
                key=os.getenv("JWT_KEY"),
                algorithms=[os.getenv("ALGORITHM")],
            )
        else:
            return msg
    except:
        return msg
