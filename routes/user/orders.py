from flask import Blueprint
from middleware.m_auth import m_auth
from controller.user.controller_order import cOrders

orders_blueprint = Blueprint("routes_orders", __name__)


@orders_blueprint.route("/order", methods=["GET"])
@m_auth
def get_orders():
    return cOrders.c_get_orders()


@orders_blueprint.route("/order/<id>", methods=["GET"])
@m_auth
def get_order_id(id):
    return cOrders.c_get_order_id(id)
