import os
import jwt
from datetime import datetime, timedelta
from utility.encrypt import fernetDecrypt
from fastapi import status, HTTPException

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def generate_token(data: dict, hours: int, min: int) -> str:
    return jwt.encode(
        payload={
            **data,
            "exp": datetime.now() + timedelta(hours=hours + 3, minutes=min),
        },
        key=os.getenv("JWT_KEY", ""),
        algorithm=os.getenv("ALGORITHM"),
    )


def valid_auth(token: str):
    try:
        data = jwt.decode(
            jwt=token.split(" ")[1] if " " in token else token,
            key=os.getenv("JWT_KEY", ""),
            algorithms=[os.getenv("ALGORITHM", "")],
        )

        if "mix" in data:
            admin_lvl = fernetDecrypt(os.getenv("ADMIN_KEY", ""), data["mix"])
            data["admin"] = admin_lvl["admin"]
            del data["mix"]

        return data
    except jwt.PyJWTError:
        raise credentials_exception
