from service.seller import service_panel

from utility.handleErr import handlerErr


def seller_panel(c_user):
    try:
        props_panel = service_panel.service_panel_seller({"id_user": c_user.id_user})
        return {
            "detail": "Informações do painel vendedor.",
            "props": props_panel,
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_panel_seller -> %s" % err)


def seller_panel_settings(form, c_user):
    try:
        data = {"id_user": c_user.id_user, **form.dict()}
        service_panel.service_panel_seller_settings(data)
        return {
            "detail": "Informações do vendedor atualizadas.",
            "status": 200,
        }
    except Exception as err:
        raise handlerErr("seller -> c_panel_seller_settings -> %s" % err)
