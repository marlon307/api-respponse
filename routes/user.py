from functools import wraps
from flask import Blueprint
from controller.contoller_user import cUser

user_blueprint = Blueprint("routes_user", __name__)
user_auth_blueprint = Blueprint("routes_user_auth", __name__)


def teste(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(args, kwargs)
        return f(*args, **kwargs)

    return decorated


@user_blueprint.route("/createuser", methods=["POST"])
def createuser():
    return cUser.c_user_register()


@user_blueprint.route("/login_user", methods=["POST"])
@teste
def login_user():
    return cUser.c_user_login()


@user_blueprint.route("/solicitation_reset_psw_user", methods=["POST"])
def solicitation_reset_psw_user():
    return cUser.c_solicitation_user_resetpsw()


@user_auth_blueprint.route("/reset_psw_user", methods=["POST"])
def reset_psw_user():
    return cUser.c_user_resetpsw()
