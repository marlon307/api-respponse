from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Header, Depends
from middleware.user.m_user import m_register, m_email, m_psw, m_update_user
from middleware.m_auth import get_current_user, m_auth
from controller.user.controller_user import cUser
from ..user.models import resp_auth, resp_user, User, resp_cUser, Default
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["USER"])


@router.post("/login_user", response_model=resp_auth)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    return cUser.c_user_login(form_data)


# @3dFt53As
@router.post("/createuser", response_model=resp_cUser)
def create_user(body: m_register):
    return cUser.c_user_register(body)


@router.patch("/confirm_acc", response_model=Default)
def confirm_acc(token: str = Header(default="Token")):
    dict = m_auth(token)
    return cUser.c_user_confirmacc(dict)


@router.post("/request_new_confirm_acc", response_model=Default)
def request_new_confirm_acc(current_user: User = Depends(get_current_user)):
    return cUser.c_request_new_confirm_acc(current_user)


@router.post("/solicitation_reset_psw_user", response_model=Default)
def solicitation_reset_psw_user(data: m_email):
    return cUser.c_solicitation_user_resetpsw(data)


@router.patch("/reset_psw_user", response_model=Default)
def reset_psw_user(data: m_psw, token: str = Header(default="Token")):
    dict = m_auth(token)
    dict["password"] = data.password
    return cUser.c_user_resetpsw(dict)


@router.get("/user", response_model=resp_user)
def get_info_user(current_user: User = Depends(get_current_user)):
    return cUser.c_get_info_user(current_user)


@router.patch("/user", response_model=Default)
def update_info_user(
    data: m_update_user, current_user: User = Depends(get_current_user)
):
    new_json = {**current_user, **jsonable_encoder(data)}
    return cUser.c_update_info_user(new_json)
