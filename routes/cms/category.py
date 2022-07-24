from flask import Blueprint
from middleware.cms.m_category import m_add_category
from controller.cms.controller_category import cCategory
from middleware.m_auth import m_auth_adm

category_cms_blueprint = Blueprint("route_product_category_cms", __name__)


@category_cms_blueprint.route("/create_category", methods=["POST"])
@m_auth_adm
@m_add_category
def add_category():
    return cCategory.c_category()
