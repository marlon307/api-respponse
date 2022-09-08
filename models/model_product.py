class qProduct:
    def q_insert_product():
        return (
            "INSERT INTO products "
            "(categorys_id, gender_id, user_id, title, subTitle, warranty, details, specifications) "
            "VALUES (%(categorys_id)s, %(gender_id)s, %(user_id)s, %(title)s, %(subTitle)s, %(warranty)s, %(details)s, %(specifications)s)"
        )

    def q_inser_product_quantity():
        return (
            "INSERT INTO quantity "
            "(sizes_id, colors_id, products_id, quantity, price, discount, url_image, sku) "
            "VALUES (%(sizes_id)s, %(colors_id)s, %(products_id)s, %(quantity)s, %(price)s, %(discount)s, %(url_image)s, %(sku)s)"
        )
