import json
from fastapi import APIRouter
import mercadopago
import os

import requests

router = APIRouter(tags=["TESTE"])


@router.post("/teste")
def rota_para_teste_rapido(data: dict):
    url = os.getenv("MELHORENVIO_API") + "api/v2/me/cart"
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
                "name": "Nome do destinatário",
                "phone": "53984470102",
                "email": "contato@melhorenvio.com.br",
                "document": "25404918047",
                "company_document": "07595604000177",
                "state_register": "123456",
                "address": "Endereço do destinatário",
                "complement": "Complemento",
                "number": "2",
                "district": "Bairro",
                "city": "Porto Alegre",
                "state_abbr": "RS",
                "country_id": "BR",
                "postal_code": "90570020",
                "note": "observação",
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
                "insurance_value": 1000.00,
                "receipt": False,
                "own_hand": False,
                "reverse": False,
                "non_commercial": True,
                "invoice": {"key": "31190307586261000184550010000092481404848162"},
                "platform": os.getenv("PLATFORM_NAME"),
                "tags": [
                    {
                        "tag": "Identificação do pedido na plataforma, exemplo: 1000007",
                        "url": "Link direto para o pedido na plataforma, se possível, caso contrário pode ser passado o valor null",
                    }
                ],
            },
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

    return data
