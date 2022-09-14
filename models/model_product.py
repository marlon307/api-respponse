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

    def q_list_prod():
        return (
            "SELECT p.id, p.title, c.category_name, "
            "JSON_ARRAYAGG(JSON_OBJECT('id', q.id, 'color_name', cl.color_name, 'color', cl.color, 'price', q.price, 'discount',q.discount, 'url_image', q.url_image)) AS color_list "
            "FROM products as p "
            "INNER JOIN categorys as c ON c.id = p.categorys_id "
            "INNER JOIN quantity as q ON q.products_id = p.id "
            "INNER JOIN colors as cl ON cl.id = q.colors_id "
            "GROUP BY p.id "
            "ORDER BY p.id DESC "
            "LIMIT 20"
        )

    def q_get_product_id():
        return (
            "SELECT p.id, p.title, c.category_name, "
            "JSON_ARRAYAGG(JSON_OBJECT('idc', cl.id, 'imgid', i.id, 'urlImg', i.url_image)) as imgs, "
            "JSON_ARRAYAGG(JSON_OBJECT('idc', cl.id, s.size, q.quantity)) as sizes, "
            "JSON_ARRAYAGG(JSON_OBJECT("
            "'idc', cl.id, "
            "'colorName' , cl.color_name, "
            "'color', cl.color,"
            "'price', q.price, "
            "'discount', q.discount,"
            "'imgs', 'teste' "
            ")) AS options "
            "FROM products as p "
            "INNER JOIN quantity as q ON q.products_id = p.id "
            "INNER JOIN categorys as c ON c.id = p.categorys_id "
            "INNER JOIN colors as cl ON cl.id = q.colors_id "
            "INNER JOIN sizes as s ON s.id = q.sizes_id "
            "INNER JOIN products_images as i ON i.quantity_id = q.id "
            "WHERE p.id = %(id)s"
            "GROUP BY q.products_id"
        )
