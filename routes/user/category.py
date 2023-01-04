from fastapi import APIRouter
from controller.user import controller_category
from ..seller.models.md_product import CategoryPage

router = APIRouter(tags=["CATEGORY"])


@router.get("/category/products", response_model=CategoryPage)
def get_products_category(category_name: str):
    return controller_category.c_categorys_products(category_name)
