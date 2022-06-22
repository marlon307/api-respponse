from flask import Blueprint, jsonify, request
from models.database import cursor, cnn
from datetime import datetime

user_blueprint = Blueprint("routes", __name__)


@user_blueprint.route("/createuser", methods=["POST"])
def createuser():
    dump_json = request.get_json()

    query = "INSERT INTO user (name, email, password) VALUES (%(name)s, %(email)s, %(password)s)"
    cursor.execute(query, dump_json)
    cnn.commit()
    cursor.close()

    return jsonify(user="resultQuery"), 200


@user_blueprint.route("/login_user", methods=["POST"])
def login_user():
    return jsonify(username="ok"), 200
