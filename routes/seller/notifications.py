from fastapi import APIRouter, Query, Request
from controller.seller import c_notification
from middleware.m_auth import User, get_current_adm
from ..user.models.md_notification import DataNotification


router = APIRouter(tags=["SELLER"])


@router.post("/notification")
def seller_notification_paymnet(
    request: Request,
    type: str = Query(None),
    id: int = Query(None),
    topic: str = Query(None),
    data: int = Query(None, alias="data.id"),
):
    resp = request.json.__dict__

    print(resp)
    data_info = {type, id, data, topic}
    return c_notification.seller_notification(data_info)
