import os
import mercadopago
from utility.insert_cart_shipping import insert_cart


def notification_seller(json, request):
    if request["action"] == "payment.updated":
        sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))
        response = sdk.payment().get(request["data"]["id"])["response"]

        if response["status"] == "approved":
            # A função abaixo deve mudar quando tiver emitindo nota fiscal
            # Mudar para outro lugar
            insert_cart(request["data"]["id"])
