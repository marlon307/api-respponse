from fastapi import status, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from auth.auth_jwt import valid_auth


class TokenData(BaseModel):
    id_user: str | None = None


class User(BaseModel):
    email: str
    id_user: str
    name: str
    seller: bool = False
    admin: bool = False


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
