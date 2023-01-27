from fastapi import APIRouter, Depends
from controller.seller import c_orders
from middleware.m_auth import User, get_current_adm
from ..user.models.md_order import (
    RListOrder,
    OrderIdSeller,
    DefaultOrder,
    UpdateStatusOrderId,
)


router = APIRouter(tags=["SELLER"])


@router.get("/seller/orders/{status}", response_model=RListOrder)
def list_order_seller(status: int, current_user: User = Depends(get_current_adm)):
    return c_orders.seller_orders(status, current_user)


@router.get("/seller/order/{id}", response_model=OrderIdSeller)
def list_order_seller(id: int, current_user: User = Depends(get_current_adm)):
    return c_orders.seller_order_id(id, current_user)


@router.patch("/seller/update_status/{id}", response_model=DefaultOrder)
def update_status_order_id_seller(
    id: int,
    statusOrder: UpdateStatusOrderId,
    current_user: User = Depends(get_current_adm),
):
    return c_orders.seller_order_id_update_status(id, statusOrder.dict(), current_user)
