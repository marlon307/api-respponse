from flask import Blueprint
from middleware.cms.m_gender import m_add_gender
from controller.cms.controller_gender import cGender
from middleware.m_auth import m_auth

gender_cms_blueprint = Blueprint("route_product_gender_cms", __name__)


@gender_cms_blueprint.route("/create_gender", methods=["POST"])
@m_auth
@m_add_gender
def add_gender():
    return cGender.c_gender()
