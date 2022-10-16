from pydantic import BaseModel


class m_add_category(BaseModel):
    c_image: str
    c_name: str
    c_title: str
    c_path: str
    c_color: str
