from ..user.user import user_blueprint
from ..user.address import address_blueprint
from ..user.cards import cards_blueprint
from ..user.bag import bag_blueprint
from ..user.orders import orders_blueprint


def blue_print_user(app):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(address_blueprint)
    app.register_blueprint(cards_blueprint)
    app.register_blueprint(bag_blueprint)
    app.register_blueprint(orders_blueprint)
