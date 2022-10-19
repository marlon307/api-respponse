from fastapi import status, HTTPException
from service.seller import service_product

msgErr500 = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Server error.",
)


def product(json: dict, files):
    try:
        service_product.create_product(json, files)
        return {
            "detail": "Produto criado com sucesso.",
            "status": 201,
        }
    except Exception as err:
        print("seller -> create_product ->", err)
        raise msgErr500


def list_product():
    try:
        list_product = service_product.list_product()
        return {
            "list": list_product,
            "detail": "Produto listado.",
            "status": 200,
        }
    except Exception as err:
        print("seller -> list_product ->", err)
        raise msgErr500


def get_product_id(id_product):
    try:
        product_id = service_product.get_product_id(id_product)
        return {
            "product": product_id,
            "detail": "Produto listado.",
            "status": 200,
        }
    except Exception as err:
        print("seller -> get_product_id ->", err)
        raise msgErr500


def options():
    try:
        list_options = service_product.list_option()
        return {
            "detail": "Lista de opções.",
            "option_list": list_options,
            "status": 200,
        }
    except Exception as err:
        print("seller -> c_list_options_seller_register_product ->", err)
        raise msgErr500
