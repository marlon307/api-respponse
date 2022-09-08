from flask import Blueprint
from controller.seller.c_product import cProduct
from middleware.m_auth import m_auth_adm

seller_product_blueprint = Blueprint("route_seller_product_create", __name__)


@seller_product_blueprint.route("/product_seller", methods=["POST"])
@m_auth_adm
def create_product():
    return cProduct.c_product()
