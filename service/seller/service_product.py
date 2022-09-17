from flask import request
from uploads.imgur_upload import upload_image_imgur
from models.database import execut_query
from models.model_product import qProduct
import json


class sProduct:
    def s_create_product(data, files_list):
        uploaded_image = upload_image_imgur(files_list)

        data["id_user"] = request.headers["user"]["id_user"]
        get_options = json.loads(data["options"])
        del data["options"]

        product_id = execut_query.insert(qProduct.q_insert_product(), data)

        def map_function(object_opt):
            return {
                "products_id": product_id,
                "price": object_opt["price"],
                "discount": object_opt["price"],
                "sku": object_opt["sku"],
                "quantity": object_opt["quantity"],
                "colors_id": object_opt["id"],
                "url_image": "https://url.image",
            }

        format_option = map(map_function, get_options)
        list_options_ids = execut_query.insertMany(
            qProduct.q_insert_product_option(), format_option
        )

        def map_has_sizes(id_option, option):
            list_s = list()
            for id_sizes in option["sizes"]:
                list_s.append(
                    {
                        "options_product_id": id_option,
                        "sizes_id": id_sizes,
                    }
                )
            return list_s

        format_has_size = map(map_has_sizes, list_options_ids, get_options)
        execut_query.insertMany(
            qProduct.q_insert_option_has_sizes(), sum(list(format_has_size), [])
        )

        def map_img_function(l_img, option_id):
            return {
                "option_id": option_id,
                "url_image": l_img["link"],
                "key_img": l_img["deletehash"],
                "upload_id": l_img["id"],
            }

        format_list_img = map(map_img_function, uploaded_image, list_options_ids)
        execut_query.insertMany(qProduct.q_insert_image(), format_list_img)

        return product_id

    def s_list_product():
        list_product = execut_query.select(qProduct.q_list_prod(), {})
        new_list = list()

        for list_obj in list_product:
            conver_str_for_json = json.loads(list_obj["color_list"])
            conver_str_for_json.sort(
                key=lambda color_list: color_list["discount"], reverse=True
            )
            new_list.append(
                {
                    **list_obj,
                    "color_list": conver_str_for_json,
                }
            )

        return new_list

    def s_get_product_id(id):
        list_product = execut_query.selectOne(qProduct.q_get_product_id(), {"id": id})
        list_product["list_images"] = json.loads(list_product["list_images"])
        list_product["list_options"] = json.loads(list_product["list_options"])
        list_product["list_sizes"] = json.loads(list_product["list_sizes"])

        print(list_product)

        return list_product
