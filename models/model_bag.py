q_check_prod_bag = """SELECT * FROM bag WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s) AND option_product_id = %(product_option)s AND orders_id IS NULL"""

q_insert_bag = """INSERT INTO bag (user_id, quantity, option_product_id, sizes_id) 
    VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1), %(quantity)s, %(product_option)s, (SELECT id FROM sizes WHERE size = %(size)s))"""

q_list_bag = """SELECT DISTINCT p.id, op.id AS opt_id, op.products_id, p.title, b.quantity, s.size, op.price, 
    op.discount, c.color, c.color_name, ctg.category_name, ophs.quantity AS max_quantity, img.url_image 
    FROM respponse_db.bag AS b 
    INNER JOIN sizes AS s ON s.id = b.sizes_id 
    INNER JOIN options_product AS op ON op.id = b.option_product_id 
    INNER JOIN options_product_has_sizes AS ophs ON ophs.options_product_id = op.id AND ophs.sizes_id = s.id 
    INNER JOIN products AS p ON p.id = op.products_id 
    INNER JOIN colors AS c ON c.id = op.colors_id 
    INNER JOIN categorys As ctg ON ctg.id = p.categorys_id 
    INNER JOIN LATERAL (SELECT option_id, url_image FROM products_images AS im WHERE im.option_id = op.id LIMIT 1) AS img ON img.option_id = op.id 
    WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) 
    AND b.orders_id IS NULL"""

q_get_producs_carrier = """SELECT op.price AS insurance_value, op.products_id AS id, op.width, op.height, op.length, op.weight, b.quantity 
    FROM options_product AS op 
    INNER JOIN bag AS b ON b.option_product_id = op.id 
    WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND b.orders_id IS NULL OR b.orders_id = %(id_order)s"""

q_main_add_bag = """SELECT DISTINCT ad.id, ad.name_delivery, ad.city, ad.district, ad.state, ad.zipcode, ad.street, ad.number_home, ad.deleted 
    FROM user_address AS ad 
    WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) AND main = 1 LIMIT 1"""

q_carrie_bag = """SELECT id, name_carrier FROM carrier"""

q_bag_update_quantity = """UPDATE bag SET quantity = %(quantity)s WHERE 
    user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND option_product_id = %(product_option)s 
    AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s) 
    AND orders_id IS NULL"""

q_bag_delete_item = """DELETE FROM bag WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND option_product_id = %(product_option)s 
    AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s) 
    AND orders_id IS NULL"""
