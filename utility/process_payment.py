import os
import mercadopago
from models.database import MySQLCnn
from models import model_orders

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
        # "notification_url": "https://respponse.marlon307.repl.co/notification",
        "payer": {
            "email": "email@emaiil.com",
            # "email": iOrder[
            #     "email"
            # ],  # o email do vendedor não pode ser o mesmo que o comprador
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

    execut_query = MySQLCnn()
    execut_query.update(
        model_orders.q_update_payment_order, (payment["id"], iOrder["number_order"])
    )
    execut_query.finishExecution()
    return payment


# https://www.mercadopago.com.br/developers/pt/docs/checkout-bricks/payment-brick/additional-customization/preferences
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
        "transaction_amount": round(iOrder["card"]["transaction_amount"], 2),
        "token": iOrder["card"]["token"],
        "description": "Pedido #%s" % (iOrder["number_order"]),
        "installments": iOrder["card"]["installments"],
        # "notification_url": "https://respponse.marlon307.repl.co/notification",
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

    execut_query = MySQLCnn()
    execut_query.update(
        model_orders.q_update_payment_order, (payment["id"], iOrder["number_order"])
    )
    execut_query.finishExecution()
    # Não retorna nada pois é um processo de segundo plano e não vai para o front-end
