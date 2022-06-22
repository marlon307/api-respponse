from flask import Blueprint, jsonify
from models.model_user import User

user_blueprint = Blueprint("routes", __name__)


@user_blueprint.route("/createuser", methods=["GET"])
def createuser():
    result = User.query.first()
    return jsonify(user=User.to_json(result)), 200


@user_blueprint.route("/login_user", methods=["POST"])
def login_user():
    return jsonify(username="ok"), 200
