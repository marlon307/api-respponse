import os
import mercadopago
from models.database import MySQLCnn
from models import model_orders
from utility.insert_cart_shipping import insert_cart


def notification_seller(json, request):
    if request["action"] == "payment.updated":
        sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))
        response = sdk.payment().get(request["data"]["id"])["response"]

        if response["status"] == "approved":
            insert_cart(request["data"]["id"])
