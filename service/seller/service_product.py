from uploads.imgur_upload import upload_image_imgur
from models.database import execut_query
from models import model_product, model_seller
from utility.calca_discount import calc_discount
from utility.unique import unique
import json


def create_product(data, files_list):
    # print(files_list[0])
    uploaded_image = upload_image_imgur(files_list)
    list_options = data["list_qtd"]
    del data["list_qtd"]

    product_id = execut_query(model_product.q_insert_product).insert(data)

    def map_function(object_opt):
        object_opt["products_id"] = product_id
        return object_opt

    format_option = map(map_function, list_options)

    list_options_ids = execut_query(model_product.q_insert_product_option).insertMany(
        list(format_option)
    )

    def map_has_sizes(id_option, option):
        new_opt = dict()
        new_opt["options_product_id"] = id_option
        new_opt["quantity"] = option["quantity"]
        new_opt["sizes_id"] = option["sizes_id"]
        return new_opt

    format_has_size = map(map_has_sizes, list_options_ids, list_options)

    execut_query(model_product.q_insert_option_has_sizes).insertMany(
        list(format_has_size)
    )

    def map_img_function(l_img, option_id):
        return {
            "option_id": option_id,
            "url_image": l_img["link"],
            "key_img": l_img["deletehash"],
            "upload_id": l_img["id"],
        }

    format_list_img = map(map_img_function, uploaded_image, list_options_ids)
    execut_query(model_product.q_insert_image).insertMany(list(format_list_img))

    return product_id


def list_product():
    list_product = execut_query(model_product.q_list_prod).select({})
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


def get_product_id(id):
    # *******************************************************************
    # ***************Favor montar uma query mais decente*****************
    # *******************************************************************
    list_product = execut_query(model_product.q_get_product_id).selectOne({"id": id})
    list_product["list_options"] = unique(json.loads(list_product["list_options"]))
    list_product["list_images"] = unique(json.loads(list_product["list_images"]))
    list_product["list_sizes"] = unique(json.loads(list_product["list_sizes"]))

    def mount_obj_size(id_option):
        size_obj = dict()
        for obj in list_product["list_sizes"]:
            if id_option == obj["option_id"]:
                size_obj = {**size_obj, **obj}
                del size_obj["option_id"]

        return size_obj

    def fomat_option(object_option):
        old_price = calc_discount(object_option["discount"], object_option["price"])
        return {
            **object_option,
            "discount": object_option["discount"],
            "oldPrice": old_price,
            "sizes": mount_obj_size(object_option["option_id"]),
            "images": list(
                filter(
                    None,
                    [
                        obj if obj["option_id"] == object_option["option_id"] else None
                        for obj in list_product["list_images"]
                    ],
                )
            ),
        }

    new_list_option = map(fomat_option, list_product["list_options"])

    list_product["list_options"] = list(new_list_option)
    del list_product["list_sizes"]
    del list_product["list_images"]
    return list_product


def list_option():
    object_lists = execut_query(model_seller.q_list_options).selectOne({"info": None})
    object_lists["list_colors"] = json.loads(object_lists["list_colors"] or "[]")
    object_lists["list_ctg"] = json.loads(object_lists["list_ctg"] or "[]")
    object_lists["list_gender"] = json.loads(object_lists["list_gender"] or "[]")
    object_lists["list_sizes"] = json.loads(object_lists["list_sizes"] or "[]")
    return object_lists
