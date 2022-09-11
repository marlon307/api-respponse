from base64 import b64encode
from flask import request
import os
from models.database import execut_query
from models.model_product import qProduct
import requests
import json


class sProduct:
    def s_create_product(data, files_list):
        # https://api.imgur.com/oauth2/authorize?client_id=4d5605fbedd6974&response_type=token
        url = "https://api.imgur.com/3/image"
        headers = {"Authorization": f"Bearer %" % os.getenv("AUTH_TOKEN_IMGUR")}
        payload = {
            "name": "Teste",
            "title": "title teste",
            "description": "description",
            "image": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        }
        response = requests.post(
            url=url,
            headers=headers,
            data=payload,
            # files=[files_list],
        )

        print(response.json())

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

        return product_id
