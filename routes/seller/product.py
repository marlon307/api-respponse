from fastapi import APIRouter, File, Form, status, HTTPException, Depends
import json
from pydantic import ValidationError
from controller.seller import c_product
from middleware.m_auth import User, get_current_adm
from ..seller.models.md_product import CreateProduct, ListProductSeller
from .models import Default, ProductId, ListProduct, OptionProduct

router = APIRouter(tags=["SELLER"])

msgErr415 = HTTPException(
    status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    detail="Server error.",
)


@router.post("/product", status_code=201)
def create_product(
    files: list[bytes] = File(),
    data: CreateProduct = Depends(CreateProduct.fields_product),
    current_user: User = Depends(get_current_adm),
):
    try:
        serialize_json = json.loads(data.json())
        serialize_json["id_user"] = current_user.id_user
        return c_product.product(serialize_json, files)
    except ValidationError as e:
        print("Route -> product: ", e.raw_errors)
        raise msgErr415


@router.get("/product", response_model=ListProduct)
def list_product():
    return c_product.list_product()


@router.get("/product/list_options")
def list_options():
    return c_product.options()


@router.get("/product/{id}", response_model=ProductId)
def get_product_id(id: int):
    return c_product.get_product_id(id)


@router.get("/seller/products", response_model=ListProductSeller)
def get_product_id(current_user: User = Depends(get_current_adm)):
    return c_product.get_products_seller(current_user.id_user)
