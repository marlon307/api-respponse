from flask import Blueprint
from middleware.m_auth import m_auth
from middleware.user.m_cards import m_cards
from controller.user.controller_cards import cCards

cards_blueprint = Blueprint("routes_cards", __name__)


@cards_blueprint.route("/add_card", methods=["POST"])
@m_auth
@m_cards
def add_cards():
    return cCards.c_add_cards()
