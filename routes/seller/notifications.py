from fastapi import APIRouter, Depends, Query
from controller.seller import c_notification
from middleware.m_auth import User, get_current_adm
from ..user.models.md_notification import DataNotification
from ..user.models.md_order import RListOrder


router = APIRouter(tags=["SELLER"])

# /notification?data.id=1312077069&order_id=200&type=payment


# def teste(id):
#     return id


@router.post("/notification")
def seller_notification_paymnet(
    order_id: int,
    type: str = Query(None),
    id: int = Query(None),
    topic: str = Query(None),
    data: int = Query(None, alias="data.id"),
):
    print(order_id, type, data, 111)
    return c_notification.seller_notification(order_id, topic, id)
