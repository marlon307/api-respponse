from flask import Blueprint
from middleware.cms.m_color import m_add_color
from controller.cms.controller_color import cColor
from middleware.m_auth import m_auth

color_cms_blueprint = Blueprint("route_product_color_cms", __name__)


@color_cms_blueprint.route("/add_color", methods=["POST"])
@m_auth
@m_add_color
def add_color():
    return cColor.c_color()
