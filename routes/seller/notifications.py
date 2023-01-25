from fastapi import APIRouter, Depends
from controller.seller import c_notification
from middleware.m_auth import User, get_current_adm
from ..user.models.md_order import RListOrder


router = APIRouter(tags=["SELLER"])


@router.post("/notification")
def seller_notification_paymnet(order_id: int, topic: str, id: int):
    return c_notification.seller_notification(topic, id)
