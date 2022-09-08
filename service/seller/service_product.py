from models.database import execut_query
from models.model_product import qProduct
import json


class sProduct:
    def s_create_product(data):
        get_list = data["list_qtd"]
        del data["list_qtd"]

        product_id = execut_query.insert(qProduct.q_insert_product(), data)

        def map_function(object_qtd):
            return {"products_id": product_id, **object_qtd}

        format_size = map(map_function, get_list)
        execut_query.insertMany(qProduct.q_inser_product_quantity(), format_size)

        return product_id
