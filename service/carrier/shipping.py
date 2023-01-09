import json
import os
import requests
from models import model_bag
from models.database import MySQLCnn


def s_calc_shipping(data):
    execut_query = MySQLCnn()
    list_products = execut_query.select(
        model_bag.q_get_producs_carrier,
        {
            "user_id": data["user_id"],
            "id_order": data["order_id"] if "order_id" in data else None,
        },
    )
    execut_query.finishExecution()

    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/calculate"
    payload = json.dumps(
        {
            "from": {"postal_code": os.getenv("MELHORENVIO_ZIPCODE")},
            "to": {"postal_code": data["zipcode"]},
            "products": list_products,
            "services": str(data["services"]) if "services" in data else "",
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

    if type(data) is list:
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
    return data


def s_add_shipping():
    pass
