from flask import request
from uploads.imgur_upload import upload_image_imgur
from models.database import execut_query
from models.model_product import qProduct
import json


class sProduct:
    def s_create_product(data, files_list):
        uploaded_image = upload_image_imgur(files_list)

        data = json.loads(data)
        data["id_user"] = request.headers["user"]["id_user"]
        get_list = data["list_qtd"]
        del data["list_qtd"]

        product_id = execut_query.insert(qProduct.q_insert_product(), data)

        def map_function(object_qtd):
            return {
                "products_id": product_id,
                "url_image": uploaded_image[0]["link"],
                **get_list[object_qtd],
            }

        format_size = map(map_function, get_list)
        result = execut_query.insertMany(
            qProduct.q_insert_product_quantity(), format_size
        )

        def map_img_function(l_img):
            index_color = l_img["ref_color"].replace("list_file-", "")
            index = int(index_color) - 1

            return {
                "quantity_id": result[index],
                "url_image": l_img["link"],
                "key_img": l_img["deletehash"],
                "upload_id": l_img["id"],
            }

        format_list_img = map(map_img_function, uploaded_image)
        execut_query.insertMany(qProduct.q_insert_image(), format_list_img)

        return product_id
