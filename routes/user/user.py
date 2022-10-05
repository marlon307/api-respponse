from fastapi import APIRouter, status, Header, Depends, HTTPException
from middleware.user.m_user import m_login, m_register, m_email, m_psw, m_update_user
from middleware.m_auth import m_auth
from controller.user.controller_user import cUser
import jwt
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


router = APIRouter(tags=["USER"])


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/login_user")
def login_user(data: OAuth2PasswordRequestForm = Depends()):
    return cUser.c_user_login()


@router.post("/createuser", status_code=status.HTTP_201_CREATED)
def create_user(body: m_register):
    return cUser.c_user_register(body)


# Need Authorization
@router.patch("/confirm_acc")
def confirm_acc(authorization: str = Header(default="Bearer token")):
    return cUser.c_user_confirmacc()


@router.post("/request_new_confirm_acc")
def request_new_confirm_acc(data: m_email):
    return cUser.c_request_new_confirm_acc()


@router.post("/solicitation_reset_psw_user")
def solicitation_reset_psw_user(data: m_email):
    return cUser.c_solicitation_user_resetpsw()


# Need Authorization
@router.patch("/reset_psw_user")
def reset_psw_user(data: m_psw):
    return cUser.c_user_resetpsw()


# Need Authorization
@router.get("/user")
def get_info_user(current_user: User = Depends(get_current_active_user)):
    return cUser.c_get_info_user()


# Need Authorization
@router.patch("/user")
def update_info_user(
    data: m_update_user, current_user: User = Depends(get_current_active_user)
):
    return cUser.c_update_info_user()
