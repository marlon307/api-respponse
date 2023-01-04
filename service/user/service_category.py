import json
from models.database import MySQLCnn
from models import model_category


def s_get_categorys_product(data):
    execut_query = MySQLCnn()
    list_prod = execut_query.select(model_category.q_list_prod_category, data)
    execut_query.finishExecution()

    def format_json(obj):
        obj["color_list"] = json.loads(obj["color_list"])
        return obj

    list_prod = map(format_json, list_prod)

    return list(list_prod)
