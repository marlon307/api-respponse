from models.database import execut_query
from models import model_seller
import json


def s_list_option():
    object_lists = execut_query(model_seller.q_list_options).selectOne({"info": None})

    object_lists["list_colors"] = json.loads(object_lists["list_colors"] or "[]")
    object_lists["list_ctg"] = json.loads(object_lists["list_ctg"] or "[]")
    object_lists["list_gender"] = json.loads(object_lists["list_gender"] or "[]")
    object_lists["list_sizes"] = json.loads(object_lists["list_sizes"] or "[]")

    return object_lists
