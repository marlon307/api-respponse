from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from controller.seller.c_product import cProduct
from middleware.m_auth import User, get_current_adm
from middleware.seller.m_product import m_create_product
from .models import Default

router = APIRouter(tags=["SELLER"])


@router.post("/product", response_model=Default, status_code=201)
def create_product(
    data: m_create_product, current_user: User = Depends(get_current_adm)
):
    return cProduct.c_product(jsonable_encoder(data))


@router.get("/product")
def list_product():
    return cProduct.c_list_product()


@router.get("/product/{id}")
def get_product_id(id: int):
    return cProduct.c_get_product_id(id)
