from flask import Blueprint
from controller.seller.c_product import cProduct
from middleware.m_auth import m_auth_adm
from middleware.seller.m_product import m_create_product

seller_product_blueprint = Blueprint("route_seller_product_create", __name__)


@seller_product_blueprint.route("/product_seller", methods=["POST"])
@m_auth_adm
# @m_create_product
def create_product():
    return cProduct.c_product()


@seller_product_blueprint.route("/list_product", methods=["GET"])
def list_product():
    return cProduct.c_list_product()
