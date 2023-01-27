from fastapi import APIRouter, Depends
from controller.seller import c_orders
from middleware.m_auth import User, get_current_adm
from ..user.models.md_order import RListOrder, OrderIdSeller


router = APIRouter(tags=["SELLER"])


@router.get("/seller/orders/{status}", response_model=RListOrder)
def list_order_seller(status: int, current_user: User = Depends(get_current_adm)):
    return c_orders.seller_orders(status, current_user)


@router.get("/seller/order/{id}", response_model=OrderIdSeller)
def list_order_seller(id: int, current_user: User = Depends(get_current_adm)):
    return c_orders.seller_order_id(id, current_user)
