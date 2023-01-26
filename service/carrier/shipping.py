import json
import os
import requests
from models import model_bag, model_carrier
from models.database import MySQLCnn
from utility.generate_volume import cube_volumes


def s_calc_shipping(data):
    execut_query = MySQLCnn()
    list_products = execut_query.select(
        model_bag.q_get_producs_carrier,
        {
            "user_id": data["user_id"],
            "id_order": data["order_id"] if "order_id" in data else None,
        },
    )
    list_box = execut_query.select(model_carrier.q_select_box, {})
    execut_query.finishExecution()
    total_volume = sum(
        map(lambda x: x["width"] + x["height"] + x["length"], list_products)
    )

    total_weight = sum(map(lambda x: x["quantity"] * x["weight"], list_products))
    box_generate = cube_volumes(total_volume, list_box, total_weight)
    insurance_value = sum(map(lambda x: x["price"] * x["quantity"], list_products))

    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/calculate"
    payload = json.dumps(
        {
            "from": {"postal_code": os.getenv("MELHORENVIO_ZIPCODE")},
            "to": {"postal_code": data["zipcode"]},
            "package": box_generate,
            "options": {"insurance_value": insurance_value},
        }
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % (os.getenv("MELHORENVIO_TOKEN")),
        "User-Agent": os.getenv("MELHORENVIO_EMAIL_SUPORTE"),
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()

    new_list = list()
    for carrier in data:
        if "error" not in carrier:
            new_list.append(
                {
                    "id": carrier["id"],
                    "name_carrier": carrier["company"]["name"],
                    "toDate": carrier["custom_delivery_time"],
                    "price": float(carrier["price"]),
                }
            )

    return new_list
