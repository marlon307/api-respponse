from fastapi import FastAPI, status, Header
from middleware.user.m_user import m_login, m_register, m_email, m_psw, m_update_user
from middleware.m_auth import m_auth
from controller.user.controller_user import cUser


def user_routes(app: FastAPI):
    @app.post("/createuser", status_code=status.HTTP_201_CREATED)
    def createuser(body: m_register):
        return cUser.c_user_register(body)

    # # Need Authorization
    @app.patch("/confirm_acc")
    def confirm_acc(authorization: str = Header(default="Bearer token")):
        return cUser.c_user_confirmacc()

    @app.post("/request_new_confirm_acc")
    def request_new_confirm_acc(data: m_email):
        return cUser.c_request_new_confirm_acc()

    # @app.route("/login_user", methods=["POST"])
    # @m_login
    # def login_user():
    #     return cUser.c_user_login()

    # @app.route("/solicitation_reset_psw_user", methods=["POST"])
    # @m_email
    # def solicitation_reset_psw_user():
    #     return cUser.c_solicitation_user_resetpsw()

    # # Need Authorization
    # @user_route.route("/reset_psw_user", methods=["PATCH"])
    # @m_auth
    # @m_psw
    # def reset_psw_user():
    #     return cUser.c_user_resetpsw()

    # @user_route.route("/user", methods=["GET"])
    # @m_auth
    # def get_info_user():
    #     return cUser.c_get_info_user()

    # @user_route.route("/user", methods=["PATCH"])
    # @m_auth
    # @m_update_user
    # def update_info_user():
    #     return cUser.c_update_info_user()
