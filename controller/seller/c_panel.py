from service.seller import service_panel

from utility.handleErr import handlerErr


def seller_panel(c_user):
    try:
        props_panel = service_panel.service_panel_seller({"id_user": c_user.id_user})
        return {
            "detail": "Informações do panel vendedor.",
            "props": props_panel,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_list_options_seller_register_product -> %s" % err)
