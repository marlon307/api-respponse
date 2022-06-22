from flask import Blueprint, jsonify, request
from models.model_user import User

user_blueprint = Blueprint("routes", __name__)


@user_blueprint.route("/createuser", methods=["POST"])
def createuser():
    json = request.get_json()
    User.register_user(json)
    return jsonify(user="Usuario Cadastrado com sucesso! ; )"), 200


@user_blueprint.route("/login_user", methods=["POST"])
def login_user():
    return jsonify(username="ok"), 200
