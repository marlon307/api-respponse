class qOrder:
    def q_get_orders():
        return (
            "SELECT o.id, date_order, s.status "
            "FROM orders AS o "
            "INNER JOIN status AS s ON s.id = o.status_id "
            "WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
            "ORDER BY o.id DESC"
        )

    def q_get_order_id():
        return (
            "SELECT o.id, o.status_id, o.date_order, o.value_order, "
            "JSON_OBJECT('name_delivery', uadd.name_delivery, 'city', uadd.city, 'district', uadd.district, "
            "'uf', uadd.uf, 'zipcode', uadd.cep, 'number_home', uadd.number_home, 'road', uadd.road) AS address, "
            "JSON_OBJECT('name_carrier', crr.name_carrier, 'code', o.tracking_code, 'delivery_value', o.delivery_value) AS carrier, "
            "JSON_ARRAYAGG(JSON_OBJECT( "
            "'title', p.title, 'category_name', ctg.category_name, 'id', p.id, "
            "'size', sz.size, 'quantity', b.quantity, "
            "'url_image', img.url_image, 'color', cl.color, "
            "'color_name', cl.color_name, 'price', op.price "
            ")) AS list_products "
            "FROM orders AS o "
            "INNER JOIN user_address AS uadd ON uadd.id = o.user_id "
            "INNER JOIN carrier AS crr ON crr.id = o.carrier_id "
            "INNER JOIN bag AS b ON b.orders_id = o.id "
            "INNER JOIN options_product AS op ON op.id = b.option_product_id "
            "INNER JOIN products AS p ON p.id = op.products_id "
            "INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id "
            "INNER JOIN sizes AS sz ON sz.id = b.sizes_id "
            "INNER JOIN products_images AS img ON img.id = b.option_product_id "
            "INNER JOIN colors AS cl ON cl.id = op.colors_id "
            "WHERE o.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) AND o.id = %(order_id)s "
            "GROUP BY o.id"
        )
