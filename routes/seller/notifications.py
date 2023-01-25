from fastapi import APIRouter, Depends
from controller.seller import c_notification
from middleware.m_auth import User, get_current_adm
from ..user.models.md_notification import DataNotification
from ..user.models.md_order import RListOrder


router = APIRouter(tags=["SELLER"])

# /notification?data.id=1312077069&order_id=200&type=payment


@router.post("/notification")
def seller_notification_paymnet(
    order_id: int,
    data: DataNotification,
    topic: str | None,
    id: int | None,
    type: str | None,
):
    print(order_id, data, type)
    return c_notification.seller_notification(order_id, topic, id)
