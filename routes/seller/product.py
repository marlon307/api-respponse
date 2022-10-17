from fastapi import APIRouter, File, Form
from fastapi.encoders import jsonable_encoder
from controller.seller import c_product
from middleware.m_auth import User, get_current_adm
from middleware.seller.m_product import m_create_product
from .models import Default

router = APIRouter(tags=["SELLER"])


@router.post("/product", response_model=Default, status_code=201)
def create_product(
    file: list[bytes] = File(description="Multiple files as UploadFile"),
    data: m_create_product = Form()
    # data: m_create_product,
    # current_user: User = Depends(get_current_adm)
):
    print(file, data)
    return {"detail": "ok", "status": 200}
    # return c_product.product(jsonable_encoder(data))


@router.get("/product")
def list_product():
    return c_product.list_product()


@router.get("/product/{id}")
def get_product_id(id: int):
    return c_product.get_product_id(id)
