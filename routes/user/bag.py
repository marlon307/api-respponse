from flask import Blueprint
from middleware.m_auth import m_auth
from controller.user.controller_bag import cBag

bag_blueprint = Blueprint("routes_bag", __name__)


@bag_blueprint.route("/bag", methods=["POST"])
@m_auth
def additembag():
    return cBag.c_add_bag()


@bag_blueprint.route("/bag", methods=["GET"])
@m_auth
def listbag():
    return cBag.c_list_bag()


@bag_blueprint.route("/bag", methods=["PATCH"])
@m_auth
def updatequantity():
    return cBag.c_bag_update_quantity()


@bag_blueprint.route("/bag", methods=["DELETE"])
@m_auth
def deleteitembag():
    return cBag.c_bag_delete()
