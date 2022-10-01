from fastapi import FastAPI
from routes.cms.blue_print_cms import blue_print_cms
from routes.user.routes import routes_user
from routes.seller.blue_print_seller import blue_print_seller


def routes(app: FastAPI) -> None:
    # ROUTERS CMS
    # blue_print_cms(app)

    # ROUTERS USERS
    routes_user(app)

    # ROUTERS SELLERS
    # blue_print_seller(app)
