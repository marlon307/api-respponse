from flask import request
import os
from models.database import execut_query
from models.model_product import qProduct
import requests
import json


class sProduct:
    def s_create_product(data, files_list):
        data = json.loads(data)
        data["id_user"] = request.headers["user"]["id_user"]

        get_list = data["list_qtd"]
        del data["list_qtd"]

        product_id = execut_query.insert(qProduct.q_insert_product(), data)

        def map_image(obj_list_image):
            return {"pack_image": obj_list_image["listImage"]}

        list_image = map(map_image, get_list)

        def map_function(object_qtd):
            del object_qtd["listImage"]
            object_qtd["url_image"] = "sds"
            return {"products_id": product_id, **object_qtd}

        format_size = map(map_function, get_list)
        result = execut_query.insertMany(
            qProduct.q_insert_product_quantity(), format_size
        )
        print(files_list)
        url = "https://api.imgur.com/3/upload"
        files = []
        payload = {"image": files}
        headers = {"Authorization": f"Client-ID %s" % os.getenv("IMIGUR_CLIENT_ID")}

        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload,
            files=files,
        )
        print(response.text)

        return product_id
