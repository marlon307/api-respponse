import os
import mercadopago

teste = {
    "number_order": 144,
    "email": "marlon-ramosb@hotmail.com",
    "cpf_cnpj": "02190634601",
    "name": "Marlon Ramos",
    "city": "Coronel Fabriciano",
    "id": 3,
    "user_id": 1,
    "name_delivery": "Marlon Ramos Teste",
    "district": "Córrego Alto",
    "state": "MG",
    "zipcode": "35170526",
    "street": "Rua Seis",
    "number_home": "128",
    "main": 0.0,
    "deleted": None,
}

# iOrder = info_order
def process_payment_pix(payment_method: str, iOrder: dict):
    sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))
    split = iOrder["name"].split()

    address = dict(
        zip_code=iOrder["zipcode"],
        street_name=iOrder["street"],
        street_number=iOrder["number_home"],
        neighborhood=iOrder["district"],
        city=iOrder["city"],
        federal_unit=iOrder["state"],
    )

    payment_data = {
        "transaction_amount": round(iOrder["price"], 2),
        "description": "Pedido #%s" % (iOrder["number_order"]),
        "payment_method_id": payment_method,
        "payer": {
            "email": "test@test.com",
            "first_name": split[0],
            "last_name": split[1],
            "identification": {
                "type": "CPF",
                "number": iOrder["cpf"],
            },
            "address": address,
        },
    }
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    return payment


def process_payment_card(payment_method: str, iOrder: dict):
    sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))
    split = iOrder["name"].split()

    address = dict(
        zip_code=iOrder["zipcode"],
        street_name=iOrder["street"],
        street_number=iOrder["number_home"],
        neighborhood=iOrder["district"],
        city=iOrder["city"],
        federal_unit=iOrder["state"],
    )

    payment_data = {
        "transaction_amount": 150,
        "token": iOrder["card"]["token"],
        "description": "Pedido #%s" % (iOrder["number_order"]),
        "installments": iOrder["card"]["installments"],
        "payment_method_id": payment_method,
        "payer": {
            "email": iOrder["card"]["payer"]["email"],
            "first_name": split[0],
            "last_name": split[1],
            "identification": {
                "type": "CPF",
                "number": iOrder["card"]["payer"]["identification"]["number"],
            },
            "address": address,
        },
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    return payment
