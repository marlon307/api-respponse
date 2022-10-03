from fastapi import FastAPI, status, Header
from middleware.user.m_user import m_login, m_register, m_email, m_psw, m_update_user
from middleware.m_auth import m_auth
from controller.user.controller_user import cUser

tags = ["USER"]


def user_routes(app: FastAPI):
    @app.post("/createuser", status_code=status.HTTP_201_CREATED, tags=tags)
    def create_user(body: m_register):
        return cUser.c_user_register(body)

    # Need Authorization
    @app.patch("/confirm_acc", tags=tags)
    def confirm_acc(authorization: str = Header(default="Bearer token")):
        return cUser.c_user_confirmacc()

    @app.post("/request_new_confirm_acc", tags=tags)
    def request_new_confirm_acc(data: m_email):
        return cUser.c_request_new_confirm_acc()

    @app.post("/login_user", tags=tags)
    def login_user(data: m_login):
        return cUser.c_user_login()

    @app.post("/solicitation_reset_psw_user", tags=tags)
    def solicitation_reset_psw_user(data: m_email):
        return cUser.c_solicitation_user_resetpsw()

    # Need Authorization
    @app.patch("/reset_psw_user", tags=tags)
    def reset_psw_user(data: m_psw):
        return cUser.c_user_resetpsw()

    # Need Authorization
    @app.get("/user", tags=tags)
    def get_info_user():
        return cUser.c_get_info_user()

    # Need Authorization
    @app.patch("/user", tags=tags)
    def update_info_user(data: m_update_user):
        return cUser.c_update_info_user()
