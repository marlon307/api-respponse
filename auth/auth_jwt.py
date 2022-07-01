import os
import jwt
from flask import request
from datetime import datetime, timedelta

msg = {
    "msg": "Acesso não autorizado!",
    "status": 401,
}, 401


def generate_token(data: object, hours: int, min: int) -> str:

    return jwt.encode(
        payload={
            **data,
            "exp": datetime.now() + timedelta(hours=hours + 3, minutes=min),
        },
        key=os.getenv("JWT_KEY"),
        algorithm=os.getenv("ALGORITHM"),
    )


def valid_auth() -> None | object:
    try:
        auth = request.headers["Authorization"]

        if "Bearer " in auth:
            data = jwt.decode(
                jwt=auth.split(" ")[1],
                key=os.getenv("JWT_KEY"),
                algorithms=[os.getenv("ALGORITHM")],
            )
            request.headers = {**request.headers, **data}

        else:
            return msg
    except Exception as err:
        print(err)
        return msg
