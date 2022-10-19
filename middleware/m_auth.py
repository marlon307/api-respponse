from fastapi import status, Depends, HTTPException
from pydantic import validator, UUID4
from fastapi.security import OAuth2PasswordBearer
from auth.auth_jwt import valid_auth
from middleware.user.m_user import ModelEmail


class User(ModelEmail):
    id_user: UUID4
    name: str
    seller: bool = False
    admin: bool = False

    @validator("id_user")
    def valid_uuid(cls, v):
        return str(v)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login_user")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return User(**valid_auth(token))
    except Exception as err:
        print("get_current_user -> ", err)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!",
        )


def m_auth(token: str):
    return valid_auth(token)


def get_current_adm(token: str = Depends(oauth2_scheme)):
    try:
        c_adm = valid_auth(token)
        if c_adm is None or "admin" not in c_adm:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized!",
            )
        return User(**c_adm)
    except Exception as err:
        print("get_current_user -> ", err)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!",
        )
