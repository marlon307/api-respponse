import json
from fastapi import APIRouter
import mercadopago
import os
from models import model_bag
from models.database import MySQLCnn

import requests

router = APIRouter(tags=["TESTE"])

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


@router.post("/teste")
def rota_para_teste_rapido(data: dict):
    to_address = teste

    execut_query = MySQLCnn()
    list_products = execut_query.select(
        model_bag.q_get_producs_carrier,
        {"user_id": 1, "id_order": 180},
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
    for product in list_products:
        new_list_calc_volumes.append({})
    print(list_products)
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
            "products": new_list_products,
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
