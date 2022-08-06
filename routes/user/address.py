from flask import Blueprint
from middleware.m_auth import m_auth
from middleware.user.m_address import m_address
from controller.user.controller_address import cAddress

address_blueprint = Blueprint("routes_address", __name__)


@address_blueprint.route("/add_address", methods=["POST"])
@m_auth
@m_address
def addaddress():
    return cAddress.c_add_address()


@address_blueprint.route("/get_address_user", methods=["GET"])
@m_auth
def getaddress():
    return cAddress.c_get_address()
