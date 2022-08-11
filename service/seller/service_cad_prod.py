from models.database import execut_query
from models.model_seller import qSeller
import json


class sAddress:
    def s_list_option(info):
        object_lists = execut_query.selectOne(
            qSeller.q_list_options(), {"user_id": info}
        )
        object_lists["list_colors"] = json.loads(object_lists["list_colors"])
        object_lists["list_ctg"] = json.loads(object_lists["list_ctg"])
        object_lists["list_gender"] = json.loads(object_lists["list_gender"])
        object_lists["list_sizes"] = json.loads(object_lists["list_sizes"])
        return object_lists
