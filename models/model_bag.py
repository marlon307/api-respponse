q_insert_bag = (
    "INSERT INTO bag (user_id, quantity, option_product_id, sizes_id) "
    "VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1), %(quantity)s, %(product_option)s, (SELECT id FROM sizes WHERE size = %(size)s))"
)

q_list_bag = (
    "SELECT CONCAT( "
    "'[',GROUP_CONCAT(DISTINCT JSON_OBJECT ( "
    "'id', lb.id,  'opt_id', lb.opt_id,  'quantity', lb.quantity, 'size', lb.size, 'price', lb.price, 'discount', lb.discount, "
    "'title', lb.title, 'category_name', lb.category_name, 'color', lb.color, 'color_name', lb.color_name, 'url_image', lb.url_image"
    ")),']') AS list_b, "
    "JSON_ARRAYAGG(JSON_OBJECT( "
    "'add_id', la.id, 'name_delivery', la.name_delivery, 'city', la.city, 'district', la.district, "
    "'uf', la.uf, 'cep', la.cep, 'road', la.road, 'number_home', la.number_home"
    ")) AS list_add "
    "FROM "
    "(SELECT p.id, o.id AS opt_id,  b.quantity, s.size, o.price, o.discount, p.title, ctg.category_name, cl.color, cl.color_name, pi.url_image, b.user_id "
    "FROM bag AS b "
    "INNER JOIN sizes AS s ON s.id = b.sizes_id "
    "INNER JOIN options_product AS o ON o.id = b.option_product_id "
    "INNER JOIN colors AS cl ON cl.id = o.colors_id "
    "INNER JOIN products AS p ON p.id = o.products_id "
    "INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id "
    "INNER JOIN products_images AS pi ON pi.option_id = o.id "
    "WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) "
    "AND b.orders_id IS NULL GROUP BY o.id, s.id) AS lb, "
    "(SELECT ad.id, ad.name_delivery, ad.city, ad.district, ad.uf, ad.cep, ad.road, ad.number_home FROM user_address AS ad WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) AND ad.deleted IS NULL) AS la"
    # "SELECT p.id, o.id AS product_option, b.quantity, s.size, o.price, o.discount, p.title,"
    # "ctg.category_name, cl.color, cl.color_name, pi.url_image "
    # "FROM bag AS b "
    # "INNER JOIN sizes AS s ON s.id = b.sizes_id "
    # "INNER JOIN options_product AS o ON o.id = b.option_product_id "
    # "INNER JOIN colors AS cl ON cl.id = o.colors_id "
    # "INNER JOIN products AS p ON p.id = o.products_id "
    # "INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id "
    # "INNER JOIN products_images AS pi ON pi.option_id = o.id "
    # "WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) "
    # "AND b.orders_id IS NULL"
)

q_bag_update_quantity = (
    "UPDATE bag SET quantity = %(quantity)s WHERE "
    "user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
    "AND option_product_id = %(product_option)s "
    "AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s)"
)

q_bag_delete_item = (
    "DELETE FROM bag WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
    "AND option_product_id = %(product_option)s "
    "AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s)"
)
