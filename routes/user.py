from flask import Blueprint
from controller.contoller_user import cUser

user_blueprint = Blueprint("routes_user", __name__)


@user_blueprint.route("/createuser", methods=["POST"])
def createuser():
    return cUser.c_user_register()


@user_blueprint.route("/login_user", methods=["POST"])
def login_user():
    return cUser.c_user_login()
