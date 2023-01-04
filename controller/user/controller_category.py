from service.user import service_category
from utility.handleErr import handlerErr


def c_categorys_products(ctg):
    try:
        list_prod_category = service_category.s_get_categorys_product({"ctg_name": ctg})
        return {
            "detail": "Lista de produdos.",
            "products_ctg": list_prod_category,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_list_options_seller_register_product -> %s" % err)
