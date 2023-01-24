from fastapi import APIRouter, Depends
from controller.seller import c_notification
from middleware.m_auth import User, get_current_adm
from ..user.models.md_order import RListOrder


router = APIRouter(tags=["SELLER"])


@router.post("/notification")
def seller_notification_paymnet(topic: str, id: int, body: dict):
    return c_notification.seller_notification(topic, id, body)
