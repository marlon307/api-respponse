from service.seller import service_list_options_prod


def c_options():
    try:
        list_options = service_list_options_prod.s_list_option()
        return {
            "detail": "Lista de opções.",
            "list": list_options,
            "status": 200,
        }, 200
    except Exception as err:
        print("seller -> c_list_options_seller_register_product ->", err)
        return {"detail": "Falha nossa.", "status": 500}
