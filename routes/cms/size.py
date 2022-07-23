from flask import Blueprint
from middleware.cms.m_size import m_add_size
from controller.cms.controller_size import cSize
from middleware.m_auth import m_auth

size_cms_blueprint = Blueprint("route_product_size_cms", __name__)


@size_cms_blueprint.route("/add_size", methods=["POST"])
@m_auth
@m_add_size
def add_size():
    return cSize.c_size()
