from fastapi import FastAPI
from routes.user import user, address, bag, orders, category
from routes.cms import color, gender, size, status, carrier, categorys
from routes.seller import product, orders_seller, panel
from routes.test import teste

# ROUTERS CMS
# blue_print_cms(app)

# ROUTERS USERS
# routes.include_router(user.router)

# ROUTERS SELLERS
# blue_print_seller(app)
def routers(app: FastAPI):
    # ROUTERS SELLERS
    app.include_router(product.router)
    app.include_router(orders_seller.router)
    app.include_router(panel.router)

    # ROUTERS CMS
    app.include_router(categorys.router)
    app.include_router(color.router)
    app.include_router(gender.router)
    app.include_router(size.router)
    app.include_router(status.router)
    app.include_router(carrier.router)

    # ROUTERS USERS
    app.include_router(user.router)
    app.include_router(address.router)
    app.include_router(bag.router)
    app.include_router(orders.router)

    # ROUTE OF PRODUCTS THAT DO NOT REQUIRE AUTHENTICATION
    app.include_router(category.router)

    # TESTE
    app.include_router(teste.router)
