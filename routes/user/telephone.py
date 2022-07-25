from flask import Blueprint
from middleware.m_auth import m_auth
from middleware.user.m_telephone import m_telephone
from controller.user.controller_telephone import cTelephone

telephone_blueprint = Blueprint("routes_telephone", __name__)


@telephone_blueprint.route("/add_telephone", methods=["POST"])
@m_auth
@m_telephone
def add_telephone():
    return cTelephone.c_add_telephone()
