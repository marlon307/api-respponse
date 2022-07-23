import ast
import os
import jwt
from flask import request
from datetime import datetime, timedelta
from utility.encrypt import fernetDecrypt
import json


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
        if (
            "Authorization" in request.headers
            and "Bearer " in request.headers["Authorization"]
        ):
            data = jwt.decode(
                jwt=request.headers["Authorization"].split(" ")[1],
                key=os.getenv("JWT_KEY"),
                algorithms=[os.getenv("ALGORITHM")],
            )

            if "mix" in data:
                admin_lvl = fernetDecrypt(os.getenv("ADMIN_KEY"), data["mix"])
                new_object = ast.literal_eval(admin_lvl)
                data["admin"] = new_object["admin"]
                del data["mix"]

            request.headers = {**request.headers, "user": data}
        else:
            return msg

    except Exception as err:
        print(err)
        return msg
