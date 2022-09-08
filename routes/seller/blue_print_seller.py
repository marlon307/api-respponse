from ..seller.list_options import list_options_blueprint
from ..seller.product import seller_product_blueprint


def blue_print_seller(app):
    app.register_blueprint(list_options_blueprint)
    app.register_blueprint(seller_product_blueprint)
