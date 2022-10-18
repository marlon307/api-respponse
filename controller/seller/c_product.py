from service.seller import service_product


def product(json: dict, files):
    try:
        # json = dict(request.form.items())
        # files = request.files

        service_product.create_product(json, files)
        return {
            "detail": "Produto criado com sucesso.",
            "status": 201,
        }
    except Exception as err:
        print("seller -> create_product ->", err)
        return {"detail": "Falha nossa.", "status": 500}


def list_product():
    try:
        list_product = service_product.list_product()
        return {
            "list": list_product,
            "detail": "Produto listado.",
            "status": 200,
        }
    except Exception as err:
        print("seller -> list_product ->", err)
        return {"detail": "Falha nossa.", "status": 500}


def get_product_id(id_product):
    try:
        product_id = service_product.get_product_id(id_product)
        return {
            "product": product_id,
            "detail": "Produto listado.",
            "status": 200,
        }
    except Exception as err:
        print("seller -> get_product_id ->", err)
        return {"detail": "Falha nossa.", "status": 500}
