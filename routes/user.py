from flask import Blueprint


user_blueprint = Blueprint("routes", __name__)


@user_blueprint.route("/createuser", methods=["POST"])
def createuser():
    return {"username": "ok"}, 200
