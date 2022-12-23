from fastapi import APIRouter
import mercadopago
import os

router = APIRouter(tags=["TESTE"])


@router.post("/teste")
def rota_para_teste_rapido():
    sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))

    # payment_data = {
    #     "transaction_amount": 100,
    #     "description": "Título do produto",
    #     "payment_method_id": "pix",
    #     "payer": {
    #         "email": "test@test.com",
    #         "first_name": "Test",
    #         "last_name": "User",
    #         "identification": {
    #             "type": "CPF",
    #             "number": "19119119100",
    #         },
    #         "address": {
    #             "zip_code": "06233-200",
    #             "street_name": "Av. das Nações Unidas",
    #             "street_number": "3003",
    #             "neighborhood": "Bonfim",
    #             "city": "Osasco",
    #             "federal_unit": "SP",
    #         },
    #     },
    # }
    token = sdk.card_token()
    print(str(token))

    payment_data = {
        "transaction_amount": 150,
        "token": "visa",
        "description": "Título do produto",
        "installments": 1,
        "payment_method_id": "visa",
        "payer": {
            "email": "email@email.com",
            "identification": {
                "type": "CPF",
                "number": "19119119100",
            },
        },
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    return payment
