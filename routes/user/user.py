from fastapi import APIRouter, Header, Depends
from middleware.user.m_user import ModelEmail, ModelPsw, ModelRegister, ModelUpUser
from middleware.m_auth import get_current_user, m_auth, User
from controller.user import controller_user
from ..user.models import resp_auth, resp_user, resp_cUser, Default
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["USER"])


@router.post("/login_user", response_model=resp_auth)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    return controller_user.user_login(form_data)


@router.post("/createuser", response_model=resp_cUser, status_code=201)
def create_user(form: ModelRegister = Depends(ModelRegister.fields_register)):
    return controller_user.user_register(form)


@router.patch("/confirm_acc", response_model=Default)
def confirm_acc(token: str = Header(default="Token")):
    dict = m_auth(token)
    return controller_user.user_confirmacc(dict)


@router.post("/request_new_confirm_acc", response_model=Default)
def request_new_confirm_acc(current_user: User = Depends(get_current_user)):
    return controller_user.request_new_confirm_acc(current_user)


@router.post("/solicitation_reset_psw_user", response_model=Default)
def solicitation_reset_psw_user(data: ModelEmail = Depends(ModelEmail.form_email)):
    return controller_user.solicitation_user_resetpsw(data)


@router.patch("/reset_psw_user", response_model=Default)
def reset_psw_user(data: ModelPsw, token: str = Header(default="Token")):
    dict = m_auth(token)
    dict["password"] = data.password
    return controller_user.user_resetpsw(dict)


@router.get("/user", response_model=resp_user)
def get_info_user(current_user: User = Depends(get_current_user)):
    return controller_user.get_info_user(current_user)


@router.patch("/user", response_model=Default)
def update_info_user(
    form: ModelUpUser = Depends(ModelUpUser.fields_update),
    current_user: User = Depends(get_current_user),
):
    new_json = {**current_user.dict(), **form.dict()}
    return controller_user.update_info_user(new_json)
