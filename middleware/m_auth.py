from fastapi import Header, status
from pydantic import BaseModel, validator
from fastapi import Header, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from auth.auth_jwt import valid_auth

msgErr = {
    "msg": "Unauthorized.",
    "status": 401,
}, 401


class TokenData(BaseModel):
    id_user: str | None = None


class User(BaseModel):
    email: str | None = None
    full_name: str | None = None
    seller: bool | None = None
    admin: bool | None = None


class m_auth(BaseModel):
    authorization: str = Header(default="Bearer token")

    @validator("authorization")
    def valid_auth_token(cls, v):
        print(v, 22222)
        pass


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login_user")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = valid_auth(token)
        return payload
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!",
        )
    # user_id: str = payload.get("id_user")
    # if user_id is None:
    #     raise payload


def m_auth_adm(f):
    # @wraps(f)
    # def decorated(*args, **kwargs):
    #     try:
    #         if valid_auth() is not None or "admin" not in request.headers["user"]:
    #             abort(401)
    #     except Exception as err:
    #         print(f"[AUTH] %s" % (err))
    #         return msgErr

    #     return f(*args, **kwargs)

    # return decorated
    return 200
