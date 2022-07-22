from flask import Blueprint
from middleware.cms.m_color import m_add_color
from controller.cms.controller_color import cColor

product_blueprint = Blueprint("route_product", __name__)


@product_blueprint.route("/add_color", methods=["POST"])
@m_add_color
def add_color():
    return cColor.c_color()
