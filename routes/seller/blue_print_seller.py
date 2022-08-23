from ..seller.list_options import list_options_blueprint


def blue_print_seller(app):
    app.register_blueprint(list_options_blueprint)
