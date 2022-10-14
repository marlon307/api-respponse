from fastapi import status, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from auth.auth_jwt import valid_auth


class TokenData(BaseModel):
    id_user: str | None = None


class User(BaseModel):
    email: str | None = None
    full_name: str | None = None
    seller: bool | None = None
    admin: bool | None = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login_user")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return valid_auth(token)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!",
        )


def m_auth(token: str):
    return valid_auth(token)


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
