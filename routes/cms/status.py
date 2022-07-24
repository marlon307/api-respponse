from flask import Blueprint
from middleware.cms.m_status import m_add_status
from controller.cms.controller_status import cStatus
from middleware.m_auth import m_auth_adm

status_cms_blueprint = Blueprint("route_product_status_cms", __name__)


@status_cms_blueprint.route("/add_status", methods=["POST"])
@m_auth_adm
@m_add_status
def add_status():
    return cStatus.c_status()
