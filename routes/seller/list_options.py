from flask import Blueprint
from controller.seller.c_list_options import cOptions
from middleware.m_auth import m_auth_adm

list_options_blueprint = Blueprint("route_seller_options_product", __name__)


@list_options_blueprint.route("/list_options", methods=["GET"])
@m_auth_adm
def list_options():
    return cOptions.c_options()
