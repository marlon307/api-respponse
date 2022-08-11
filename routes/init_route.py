from flask import Flask
from routes.user.user import user_blueprint
from routes.cms.color import color_cms_blueprint
from routes.cms.size import size_cms_blueprint
from routes.cms.category import category_cms_blueprint
from routes.cms.gender import gender_cms_blueprint
from routes.cms.status import status_cms_blueprint
from routes.user.address import address_blueprint
from routes.user.cards import cards_blueprint
from routes.seller.list_options import list_options_blueprint


def routes(app: Flask) -> None:
    # ROUTERS CMS
    app.register_blueprint(color_cms_blueprint)
    app.register_blueprint(size_cms_blueprint)
    app.register_blueprint(category_cms_blueprint)
    app.register_blueprint(gender_cms_blueprint)
    app.register_blueprint(status_cms_blueprint)

    # ROUTERS USERS
    app.register_blueprint(user_blueprint)
    app.register_blueprint(address_blueprint)
    app.register_blueprint(cards_blueprint)

    # ROUTERS SELLERS
    app.register_blueprint(list_options_blueprint)
