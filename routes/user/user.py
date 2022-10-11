from fastapi import APIRouter, status, Header, Depends, Request
from middleware.user.m_user import m_register, m_email, m_psw, m_update_user
from middleware.m_auth import get_current_user
from controller.user.controller_user import cUser
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm


class User(BaseModel):
    email: str | None = None
    full_name: str | None = None
    seller: bool | None = None
    admin: bool | None = None


router = APIRouter(tags=["USER"])


@router.post("/login_user")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    return cUser.c_user_login(form_data)


# 3!1aDf.6
@router.post("/createuser", status_code=status.HTTP_201_CREATED)
def create_user(body: m_register):
    return cUser.c_user_register(body)


# Need Authorization
@router.patch("/confirm_acc")
def confirm_acc(authorization: str = Header(default="Bearer token")):
    return cUser.c_user_confirmacc()


@router.post("/request_new_confirm_acc")
def request_new_confirm_acc(data: m_email):
    return cUser.c_request_new_confirm_acc(data)


@router.post("/solicitation_reset_psw_user")
def solicitation_reset_psw_user(data: m_email):
    return cUser.c_solicitation_user_resetpsw(data)


# Need Authorization
@router.patch("/reset_psw_user")
def reset_psw_user(data: m_psw, auth: str = Header(default="Bearer token")):
    print(auth, data)
    return cUser.c_user_resetpsw(data)


# Need Authorization
@router.get("/user")
def get_info_user(current_user: User = Depends(get_current_user)):
    return cUser.c_get_info_user(current_user)


# Need Authorization
@router.patch("/user")
def update_info_user(
    data: m_update_user, current_user: User = Depends(get_current_user)
):
    return cUser.c_update_info_user()
