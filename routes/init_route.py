from flask import Flask
from routes.cms.blue_print_cms import blue_print_cms
from routes.user.blue_print_user import blue_print_user
from routes.seller.blue_print_seller import blue_print_seller


def routes(app: Flask) -> None:
    # ROUTERS CMS
    blue_print_cms(app)

    # ROUTERS USERS
    blue_print_user(app)

    # ROUTERS SELLERS
    blue_print_seller(app)
