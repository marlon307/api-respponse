from flask import Blueprint
from middleware.m_auth import m_auth
from middleware.user.m_address import m_address
from controller.user.controller_address import cAddress

address_blueprint = Blueprint("routes_address", __name__)


@address_blueprint.route("/address", methods=["POST"])
@m_auth
@m_address
def addaddress():
    return cAddress.c_add_address()


@address_blueprint.route("/address", methods=["GET"])
@m_auth
def getaddress():
    return cAddress.c_get_address()


@address_blueprint.route("/address", methods=["DELETE"])
@m_auth
def deleteaddress():
    return cAddress.c_delete_address()
