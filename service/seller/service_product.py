from uploads.imgur_upload import upload_image_imgur
from models.database import MySQLCnn
from models import model_product, model_seller
from utility.unique import unique
import json


def create_product(data, files_list: list[bytes]):
    mImg = 6  # max image for options
    if len(files_list) % mImg == 0 and len(data["list_qtd"]) * mImg == len(files_list):
        uploaded_image = upload_image_imgur(files_list, data["title"], data["details"])

        if len(uploaded_image) % mImg == 0:  # Checar se o upload foi feito corretamente

            execut_query = MySQLCnn()
            list_options = data["list_qtd"]
            del data["list_qtd"]
            product_id = execut_query.insert(model_product.q_insert_product, data)

            def map_function(object_opt):
                return {
                    "products_id": product_id,
                    "price": object_opt["price"],
                    "discount": object_opt["discount"],
                    "sku": object_opt["sku"],
                    "colors_id": object_opt["id"],
                    "width": object_opt["width"],
                    "height": object_opt["height"],
                    "length": object_opt["length"],
                    "weight": object_opt["weight"],
                }

            format_option = map(map_function, list_options)
            list_options_ids = execut_query.insertMany(
                model_product.q_insert_product_option, format_option
            )

            def map_has_sizes(id_option, option):
                list_s = list()
                for obj_opt in option["sizes"]:
                    list_s.append(
                        {
                            "options_product_id": id_option,
                            "sizes_id": obj_opt["id"],
                            "quantity": obj_opt["quantity"],
                        }
                    )
                return list_s

            format_has_size = map(map_has_sizes, list_options_ids, list_options)
            execut_query.insertMany(
                model_product.q_insert_option_has_sizes, sum(list(format_has_size), [])
            )

            splited = [
                uploaded_image[i : i + mImg]
                for i in range(0, len(uploaded_image), mImg)
            ]

            def map_img_function(l_img, option_id):
                for obj_img in l_img:
                    obj_img["option_id"] = option_id

                return l_img

            format_list_img = map(map_img_function, splited, list_options_ids)

            unique_list = list()
            for l in list(format_list_img):
                unique_list.extend(l)

            execut_query.insertMany(model_product.q_insert_image, unique_list)
            execut_query.finishExecution()
            return product_id
        return False
    return False


def list_product():
    execut_query = MySQLCnn()
    list_slides = execut_query.select(model_product.q_slides, {})
    list_categorys = execut_query.select(model_product.q_categorys, {})
    list_products = execut_query.select(model_product.q_list_prod_home, {})

    execut_query.finishExecution()
    new_list = list()

    for list_obj in list_products:
        list_color = json.loads(list_obj["color_list"])
        list_color.sort(key=lambda color_list: color_list["discount"], reverse=True)
        new_list.append(
            {
                **list_obj,
                "color_list": list_color,
            }
        )

    list_products = new_list
    return {
        "slides": list_slides,
        "categorys": list_categorys,
        "list_products": list_products,
    }


def get_product_id(id):
    # *******************************************************************
    # ***************Favor montar uma query mais decente*****************
    # *******************************************************************
    execut_query = MySQLCnn()
    list_product = execut_query.selectOne(model_product.q_get_product_id, {"id": id})
    execut_query.finishExecution()

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
        return {
            **object_option,
            "discount": object_option["discount"],
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


def s_list_products_seller(id):
    execut_query = MySQLCnn()
    list_products = execut_query.selectOne(
        model_product.q_list_prod_seller, {"id_user": id}
    )
    execut_query.finishExecution()
    return list_products


def list_option():
    execut_query = MySQLCnn()
    object_lists = execut_query.selectOne(model_seller.q_list_options, {"info": None})
    execut_query.finishExecution()

    object_lists["list_colors"] = json.loads(object_lists["list_colors"] or "[]")
    object_lists["list_ctg"] = json.loads(object_lists["list_ctg"] or "[]")
    object_lists["list_gender"] = json.loads(object_lists["list_gender"] or "[]")
    object_lists["list_sizes"] = json.loads(object_lists["list_sizes"] or "[]")
    return object_lists
