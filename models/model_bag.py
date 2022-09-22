class qBag:
    def q_insert_bag():
        return (
            "INSERT INTO bag (user_id, quantity, option_product_id, sizes_id) "
            "VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1), %(quantity)s, %(product_option)s, (SELECT id FROM sizes WHERE size = %(size)s))"
        )

    def q_list_bag():
        return (
            "SELECT p.id, o.id AS product_option, b.quantity, s.size, o.price, o.discount, p.title,"
            "ctg.category_name, cl.color, cl.color_name, pi.url_image "
            "FROM bag AS b "
            "INNER JOIN sizes AS s ON s.id = b.sizes_id "
            "INNER JOIN options_product AS o ON o.id = b.option_product_id "
            "INNER JOIN colors AS cl ON cl.id = o.colors_id "
            "INNER JOIN products AS p ON p.id = o.products_id "
            "INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id "
            "INNER JOIN products_images AS pi ON pi.option_id = o.id "
            "WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1)"
        )

    def q_bag_update_quantity():
        return (
            "UPDATE bag SET quantity = %(quantity)s WHERE "
            "user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
            "AND option_product_id = %(product_option)s "
            "AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s)"
        )

    def q_bag_delete_item():
        return (
            "DELETE FROM bag WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
            "AND option_product_id = %(product_option)s "
            "AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s)"
        )