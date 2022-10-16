from fastapi import FastAPI
from routes.user import user, address, bag, orders
from routes.cms import category, color, gender, size

# ROUTERS CMS
# blue_print_cms(app)

# ROUTERS USERS
# routes.include_router(user.router)

# ROUTERS SELLERS
# blue_print_seller(app)
def routers(app: FastAPI):
    # ROUTERS CMS
    app.include_router(category.router)
    app.include_router(color.router)
    app.include_router(gender.router)
    app.include_router(size.router)

    # ROUTERS USERS
    app.include_router(user.router)
    app.include_router(address.router)
    app.include_router(bag.router)
    app.include_router(orders.router)
