import json
from fastapi import APIRouter
import mercadopago
import os
from models import model_bag, model_seller, model_carrier
from models.database import MySQLCnn

import requests

from service.carrier.shipping import s_calc_shipping

router = APIRouter(tags=["TESTE"])

teste = {
    "number_order": 200,
    "price": 353.939998626709,
    "email": "marlon-ramosb@hotmail.com",
    "cpf": "02190634601",
    "ie": "453534",
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
    "obs": "Teste 64 caract",
}


def recalc_carrier(data, order):

    new_data = {
        "services": data["carrie"],
        "user_id": data["p_userid"],
        "zipcode": order["zipcode"],
        "order_id": order["number_order"],
    }
    value_shipping = s_calc_shipping(new_data)
    print(value_shipping)

    return value_shipping["packages"]


def generateVolumes(products, boxes):
    box_mounted = list
    big_product = max(
        (p["width"] + p["height"] + p["length"]) * p["quantity"] for p in products
    )
    value = 3
    target = 5
    proximity = abs(value - target)
    print(big_product)
    return []


# def generateVolumes(products, boxes):
#     print("produtos", products)
#     print("caixas", boxes)


@router.post("/teste")
def rota_para_teste_rapido(data: dict):
    to_address = teste

    execut_query = MySQLCnn()
    list_products = execut_query.select(
        model_bag.q_get_producs_carrier,
        {"user_id": 1, "iduser": 0, "id_order": 201},
    )
    info_seller = execut_query.selectOne(
        model_seller.q_select_seller_settings, {"id_user": 0, "iduser": 1}
    )
    execut_query.finishExecution()

    url = os.getenv("MELHORENVIO_API") + "api/v2/me/cart"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % (os.getenv("MELHORENVIO_TOKEN")),
        "User-Agent": os.getenv("MELHORENVIO_EMAIL_SUPORTE"),
    }

    new_list_products = list()
    for product in list_products:
        new_list_products.append(
            {
                "name": "%s %s" % (product["category_name"], product["title"]),
                "quantity": product["quantity"],
                "unitary_value": product["insurance_value"],
                "weight": product["weight"],
            }
        )

    new_list_calc_volumes = list()
    for box in info_seller["boxes"]:
        new_list_calc_volumes.append(box)

    generateVolumes(list_products, json.loads(info_seller["boxes"]))

    seller_address = json.loads(info_seller["address"])
    payload = json.dumps(
        {
            "service": 3,
            "agency": 1166,
            "from": {
                "name": info_seller["store_name"],
                "phone": "53984470102",
                "email": info_seller["email"],
                # "document": "16571478358",
                "company_document": info_seller["cnpj"],
                "state_register": info_seller["ie"],
                "address": "Endereço do remetente",
                "complement": seller_address["complement"],
                "number": seller_address["number_home"],
                "district": seller_address["district"],
                "city": seller_address["city"],
                "country_id": "BR",
                "postal_code": seller_address["zipcode"],
                "note": info_seller["obs"],
            },
            "to": {
                "name": to_address["name"],
                "phone": "53984470102",
                "email": to_address["email"],
                "document": to_address["cpf"],
                # "company_document": "07595604000177",
                # "state_register": "123456",
                "address": "Endereço do destinatário",
                "complement": to_address["complement"],
                "number": to_address["number_home"],
                "district": to_address["district"],
                "city": to_address["city"],
                "state_abbr": to_address["state"],
                "country_id": "BR",
                "postal_code": to_address["zipcode"],
                "note": to_address["obs"],
            },
            "products": new_list_products,
            "volumes": new_list_calc_volumes,
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


def find_min_boxes(total_volume, volumes):
    # sort the volumes in descending order
    boxes = []
    volumes.sort(reverse=True)
    remaining_volume = total_volume
    # iterate through the volumes and add them to the boxes until the total volume is reached
    for volume in volumes:
        while remaining_volume >= volume:
            boxes.append(volume)
            remaining_volume -= volume

    # Se sobrar algum valor do meu volume ele irá pega a utima caixa somar com restante e procurar uma caixa maior

    if remaining_volume > 0:
        volumes.sort(reverse=False)
        if len(boxes) > 0:
            remaining_volume += boxes[-1]
            boxes.pop()

            for b in volumes:
                if b >= remaining_volume:
                    boxes.append(b)
                    break
        else:
            boxes.append(volumes[0])
    return boxes


# Example usage
total_volume = 125
volumes = [100, 20, 30, 40, 50, 60, 70, 90]
print(find_min_boxes(total_volume, volumes))
