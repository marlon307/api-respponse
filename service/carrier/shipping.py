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

    url = os.getenv("MELHORENVIO_API") + "api/v2/me/shipment/calculate"
    payload = json.dumps(
        {
            "from": {"postal_code": os.getenv("MELHORENVIO_ZIPCODE")},
            "to": {"postal_code": data["zipcode"]},
            "package": box_generate,
            "options": {"insurance_value": 1500},
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


teste = {
    "number_order": 200,
    "price": 353.939998626709,
    "email": "marlon-ramosb@hotmail.com",
    "cpf": "02190634601",
    "name": "Marlon Ramos",
    "city": "Coronel Fabriciano",
    "id": 2,
    "user_id": 1,
    "name_delivery": "Marlon Ramos",
    "district": "Corrego Alto",
    "state": "MG",
    "zipcode": "24471340",
    "street": "Rua Seis",
    "number_home": "128",
    "main": 1.0,
    "deleted": None,
    "complement": "Casa",
}


def recalc_carrier(data, order):
    new_data = {
        "services": data["carrie"],
        "user_id": data["p_userid"],
        "zipcode": order["zipcode"],
        "order_id": order["number_order"],
    }
    value_shipping = s_calc_shipping(new_data)

    execut_query = MySQLCnn()
    execut_query.update(
        model_carrier.q_update_value_shipping,
        {
            "order_id": order["number_order"],
            "delivery_value": float(value_shipping["price"]),
            "p_userid": data["p_userid"],
        },
    )
    execut_query.finishExecution()


def s_add_shipping(to_address=teste):
    url = os.getenv("MELHORENVIO_API") + "api/v2/me/cart"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % (os.getenv("MELHORENVIO_TOKEN")),
        "User-Agent": os.getenv("MELHORENVIO_EMAIL_SUPORTE"),
    }

    payload = json.dumps(
        {
            "service": 3,
            "agency": 1,
            "from": {
                "name": "Nome do remetente",
                "phone": "53984470102",
                "email": "contato@melhorenvio.com.br",
                "document": "16571478358",
                "company_document": "89794131000100",
                "state_register": "123456",
                "address": "Endereço do remetente",
                "complement": "Complemento",
                "number": "1",
                "district": "Bairro",
                "city": "São Paulo",
                "country_id": "BR",
                "postal_code": "01002001",
                "note": "observação",
            },
            "to": {
                "name": to_address["name"],
                "phone": "53984470102",
                "email": to_address["email"],
                "document": to_address["cpf"],
                "company_document": "07595604000177",
                "state_register": "123456",
                "address": "Endereço do destinatário",
                "complement": to_address["complement"],
                "number": to_address["number_home"],
                "district": to_address["district"],
                "city": to_address["city"],
                "state_abbr": to_address["state"],
                "country_id": "BR",
                "postal_code": to_address["zipcode"],
                "note": "Observação",
            },
            "products": [
                {
                    "name": "Papel adesivo para etiquetas 1",
                    "quantity": 3,
                    "unitary_value": 100.00,
                },
                {
                    "name": "Papel adesivo para etiquetas 2",
                    "quantity": 1,
                    "unitary_value": 700.00,
                },
            ],
            "volumes": [{"height": 15, "width": 20, "length": 10, "weight": 3.5}],
            "options": {
                "insurance_value": to_address["price"],
                "receipt": False,
                "own_hand": False,
                "reverse": False,
                "non_commercial": True,
                "invoice": {"key": "31190307586261000184550010000092481404848162"},
                "platform": os.getenv("PLATFORM_NAME"),
                "tags": [
                    {
                        "tag": "Pedido: %s" % to_address["number_order"],
                        "url": None,
                    }
                ],
            },
        }
    )

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()

    return data
