class qProduct:
    def q_insert_product():
        return (
            "INSERT INTO products "
            "(categorys_id, gender_id, user_id, title, warranty, details, specifications) "
            "VALUES (%(categorys_id)s, %(gender_id)s, (SELECT id FROM respponse_db.user WHERE id_user = %(id_user)s), %(title)s, %(warranty)s, %(details)s, %(specifications)s)"
        )

    def q_insert_product_quantity():
        return (
            "INSERT INTO quantity "
            "(sizes_id, colors_id, products_id, quantity, price, discount, url_image, sku) "
            "VALUES (%(sizes_id)s, %(colors_id)s, %(products_id)s, %(quantity)s, %(price)s, %(discount)s, %(url_image)s, %(sku)s)"
        )

    def q_insert_image():
        return (
            "INSERT INTO products_images "
            "(quantity_id, url_image, key_img, upload_id) "
            "VALUES (%(quantity_id)s, %(url_image)s, %(key_img)s, %(upload_id)s)"
        )
