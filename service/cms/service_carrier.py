import os
import requests
from models.database import MySQLCnn
from models import model_carrier


def formatSize(param: list[dict], id: int):
    list_sizes = list()
    for type_size in param:
        list_sizes.append(
            {
                "carrier_id": id,
                "type": type_size,
                "weight_min": param[type_size]["weight"]["min"]
                if "weight" in param[type_size]
                else 0,
                "weight_max": param[type_size]["weight"]["max"]
                if "weight" in param[type_size]
                else 0,
                "width_min": param[type_size]["width"]["min"]
                if "width" in param[type_size]
                else 0,
                "width_max": param[type_size]["width"]["max"]
                if "width" in param[type_size]
                else 0,
                "height_min": param[type_size]["height"]["min"]
                if "height" in param[type_size]
                else 0,
                "height_max": param[type_size]["height"]["max"]
                if "height" in param[type_size]
                else 0,
                "length_min": param[type_size]["length"]["min"]
                if "length" in param[type_size]
                else 0,
                "length_max": param[type_size]["length"]["max"]
                if "length" in param[type_size]
                else 0,
                "diameter_min": param[type_size]["diameter"]["min"]
                if "diameter" in param[type_size]
                else 0,
                "diameter_max": param[type_size]["diameter"]["max"]
                if "diameter" in param[type_size]
                else 0,
                "sum": param[type_size]["sum"] if "sum" in param[type_size] else 0,
            }
        )
    return list_sizes


def s_refresh_carries():
    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/companies"
    headers = {"accept": "application/json", "User-Agent": "ReadMe-API-Explorer"}
    response = requests.get(url, headers=headers)

    new_carries = list()
    new_carries_formats = list()

    for carrier in response.json():
        for service in carrier["services"]:
            new_carries.append(
                {
                    "id": service["id"],
                    "name": carrier["name"],
                    "service": service["name"],
                    "picture": carrier["picture"],
                }
            )
            new_carries_formats.extend(
                formatSize(service["restrictions"]["formats"], service["id"])
            )

    execut_query = MySQLCnn()
    execut_query.insertMany(model_carrier.q_isert_carries, new_carries)
    # execut_query.insertMany(model_carrier.q_insert_sizes, new_carries_formats)
    execut_query.finishExecution()
    return True
