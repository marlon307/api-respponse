import json
import os
import requests
from models.database import MySQLCnn
from models import model_carrier


def s_refresh_carries():
    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/companies"
    headers = {"accept": "application/json", "User-Agent": "ReadMe-API-Explorer"}
    response = requests.get(url, headers=headers)

    new_carries_format = list()
    for carrier in response.json():
        for service in carrier["services"]:
            new_carries_format.append(
                {
                    "id": service["id"],
                    "name": carrier["name"],
                    "service": service["name"],
                    "picture": carrier["picture"],
                }
            )

    execut_query = MySQLCnn()
    execut_query.insertMany(model_carrier.q_isert_carries, new_carries_format)
    execut_query.finishExecution()
    return True
