from flask import Blueprint
from middleware.user.m_user import m_login, m_register, m_email, m_psw, m_update_user
from middleware.m_auth import m_auth
from controller.user.contoller_user import cUser

user_blueprint = Blueprint("routes_user", __name__)


@user_blueprint.route("/createuser", methods=["POST"])
@m_register
def createuser():
    return cUser.c_user_register()


# Need Authorization
@user_blueprint.route("/confirm_acc", methods=["PATCH"])
@m_auth
def confirm_acc():
    return cUser.c_user_confirmacc()


@user_blueprint.route("/request_new_confirm_acc", methods=["POST"])
@m_email
def request_new_confirm_acc():
    return cUser.c_request_new_confirm_acc()


@user_blueprint.route("/login_user", methods=["POST"])
@m_login
def login_user():
    return cUser.c_user_login()


@user_blueprint.route("/solicitation_reset_psw_user", methods=["POST"])
@m_email
def solicitation_reset_psw_user():
    return cUser.c_solicitation_user_resetpsw()


# Need Authorization
@user_blueprint.route("/reset_psw_user", methods=["PATCH"])
@m_auth
@m_psw
def reset_psw_user():
    return cUser.c_user_resetpsw()


@user_blueprint.route("/get_user_info", methods=["GET"])
@m_auth
def get_info_user():
    return cUser.c_get_info_user()


@user_blueprint.route("/update_user", methods=["PATCH"])
@m_auth
@m_update_user
def update_info_user():
    return cUser.c_update_info_user()
