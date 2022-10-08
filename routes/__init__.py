from fastapi import FastAPI
from routes.user import user

# ROUTERS CMS
# blue_print_cms(app)

# ROUTERS USERS
# routes.include_router(user.router)

# ROUTERS SELLERS
# blue_print_seller(app)
def routers(app: FastAPI):
    # ROUTERS USERS
    app.include_router(user.router)
