from pydantic import BaseModel, HttpUrl


class ListImage(BaseModel):
    imgid: int
    urlImg: str
    option_id: int


class ListOption(BaseModel):
    idc: int
    color: str
    price: float
    discount: int
    colorName: str
    option_id: int
    oldPrice: float
    sizes: dict
    images: list[ListImage]


class Product(BaseModel):
    id: int
    title: str
    details: str
    specifications: str
    category_name: str
    list_options: list[ListOption]


class ProductId(BaseModel):
    product: Product
    detail: str
    status: int


# List
class ListProdColor(BaseModel):
    id: int
    color: str
    price: float
    discount: int
    url_image: str
    color_name: str


class MinInfoProductList(BaseModel):
    id: int
    title: str
    category_name: str
    color_list: list[ListProdColor]


class CategoryHome(BaseModel):
    ctgID: int
    path: str
    color: str
    categoryName: str
    sub_title: str
    imgCategory: HttpUrl


class ListProduct(BaseModel):
    list_product: list[MinInfoProductList]
    categorys: list[CategoryHome]
    detail: str
    status: int


# List Options
class Color(BaseModel):
    id: int
    color: str
    color_name: str


class Category(BaseModel):
    id: int
    color: str
    sub_title: str
    url_image: str
    category_name: str


class Gender(BaseModel):
    id: int
    gender: str
    gender_name: str


class Size(BaseModel):
    id: int
    size: str


class OptionList(BaseModel):
    list_colors: list[Color]
    list_ctg: list[Category]
    list_gender: list[Gender]
    list_sizes: list[Size]


class OptionProduct(BaseModel):
    option_list: OptionList
    detail: str
    status: int
