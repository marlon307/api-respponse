import json
import os
from fastapi import APIRouter, Depends
import requests
from controller.user import controller_bag
from middleware.m_auth import User, get_current_user
from middleware.user.m_bag import add_bag, del_bag, up_bag, r_order
from ..user.models import Default, ListBag, RgOrder


router = APIRouter(tags=["USER"])


@router.post("/bag", response_model=Default, status_code=201)
def additembag(data: add_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_add_bag(data.dict(), current_user)


@router.get("/bag", response_model=ListBag)
def listbag(current_user: User = Depends(get_current_user)):
    return controller_bag.c_list_bag(current_user)


@router.patch("/bag", response_model=Default)
def updatequantity(data: up_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_update_quantity(data.dict(), current_user)


@router.delete("/bag", response_model=Default)
def deleteitembag(data: del_bag, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_delete(data.dict(), current_user)


@router.post("/register_order", response_model=RgOrder, status_code=201)
def registerorder(data: r_order, current_user: User = Depends(get_current_user)):
    return controller_bag.c_bag_register_order(data.dict(), current_user)


@router.post("/calc", status_code=200)
def registerorder():

    url = "https://sandbox.melhorenvio.com.br/api/v2/me/shipment/calculate"

    payload = json.dumps(
        {
            "from": {"postal_code": "35170522"},
            "to": {"postal_code": "01018020"},
            "products": [
                {
                    "id": "x",
                    "width": 11,
                    "height": 17,
                    "length": 11,
                    "weight": 0.3,
                    "insurance_value": 10.1,
                    "quantity": 1,
                },
                {
                    "id": "y",
                    "width": 16,
                    "height": 25,
                    "length": 11,
                    "weight": 0.3,
                    "insurance_value": 55.05,
                    "quantity": 2,
                },
                {
                    "id": "z",
                    "width": 22,
                    "height": 30,
                    "length": 11,
                    "weight": 1,
                    "insurance_value": 30,
                    "quantity": 1,
                },
            ],
        }
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % (os.getenv("MELHORENVIO_TOKEN")),
        "User-Agent": "Aplicação (email para contato técnico)",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()
