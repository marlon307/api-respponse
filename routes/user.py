from flask import Blueprint, jsonify


user_blueprint = Blueprint("routes", __name__)


@user_blueprint.route("/createuser", methods=["POST"])
def createuser():
    return jsonify(username="ok"), 200


@user_blueprint.route("/login_user", methods=["POST"])
def login_user():
    return jsonify(username="ok"), 200
