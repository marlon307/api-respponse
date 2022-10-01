from .user import user_routes

# from .address import address_blueprint
# from .cards import cards_blueprint
# from .bag import bag_blueprint
# from .orders import orders_blueprint


def routes_user(app):
    user_routes(app)
    # app.register_blueprint(address_blueprint)
    # app.register_blueprint(cards_blueprint)
    # app.register_blueprint(bag_blueprint)
    # app.register_blueprint(orders_blueprint)
