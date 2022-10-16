from fastapi import APIRouter, Depends
from middleware.m_auth import get_current_user
from controller.user.controller_order import cOrders
from ..user.models import User

router = APIRouter(tags=["USER"])


@router.get("/order")
def get_orders(current_user: User = Depends(get_current_user)):
    return cOrders.c_get_orders(current_user)


@router.get("/order/{id}")
def get_order_id(id: int, current_user: User = Depends(get_current_user)):
    return cOrders.c_get_order_id(id, current_user)
