from fastapi import APIRouter, status, Header
from middleware.user.m_user import m_login, m_register, m_email, m_psw, m_update_user
from middleware.m_auth import m_auth
from controller.user.controller_user import cUser

router = APIRouter(tags=["USER"])


@router.post("/login_user")
def login_user(data: m_login):
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
def get_info_user():
    return cUser.c_get_info_user()


# Need Authorization
@router.patch("/user")
def update_info_user(data: m_update_user):
    return cUser.c_update_info_user()
