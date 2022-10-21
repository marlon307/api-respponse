from service.seller import service_product
from utility.handleErr import handlerErr, JSONResponse, status


def product(json: dict, files):
    try:
        result = service_product.create_product(json, files)
        if result is not False:
            return {
                "detail": "Produto criado com sucesso.",
                "status": 201,
            }
        return JSONResponse(
            content={
                "detail": "Verefique se todos os campos foram preenchido.",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as err:
        raise handlerErr("seller -> create_product -> %s" % err)


def list_product():
    try:
        list_product = service_product.list_product()
        return {
            "list": list_product,
            "detail": "Produto listado.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> list_product -> %s" % err)


def get_product_id(id_product):
    try:
        product_id = service_product.get_product_id(id_product)
        return {
            "product": product_id,
            "detail": "Produto listado.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> get_product_id -> %s" % err)


def options():
    try:
        list_options = service_product.list_option()
        return {
            "detail": "Lista de opções.",
            "option_list": list_options,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_list_options_seller_register_product -> %s" % err)
