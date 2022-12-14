q_insert_bag = """INSERT INTO bag (user_id, quantity, option_product_id, sizes_id) 
    VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1), %(quantity)s, %(product_option)s, (SELECT id FROM sizes WHERE size = %(size)s))"""

q_list_bag = """SELECT p.id, o.id AS opt_id, b.quantity, s.size, o.price, o.discount, p.title, ctg.category_name, cl.color, cl.color_name, pi.url_image, b.user_id 
    FROM bag AS b 
    INNER JOIN sizes AS s ON s.id = b.sizes_id 
    INNER JOIN options_product AS o ON o.id = b.option_product_id 
    INNER JOIN colors AS cl ON cl.id = o.colors_id 
    INNER JOIN products AS p ON p.id = o.products_id 
    INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id 
    INNER JOIN products_images AS pi ON pi.option_id = o.id 
    WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) 
    AND b.orders_id IS NULL"""

q_main_add_bag = """SELECT DISTINCT ad.id, ad.name_delivery, ad.city, ad.district, ad.state, ad.zipcode, ad.street, ad.number_home, ad.deleted 
    FROM user_address AS ad 
    WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) AND main = 1 LIMIT 1"""

q_carrie_bag = """SELECT id, name_carrier FROM carrier"""

# q_list_bag2 = """SELECT DISTINCT JSON_ARRAYAGG(JSON_OBJECT(
#     'id', lb.id,  'opt_id', lb.opt_id, 'quantity', lb.quantity, 'size', lb.size, 'price', lb.price, 'discount', lb.discount,
#     'title', lb.title, 'category_name', lb.category_name, 'color', lb.color, 'color_name', lb.color_name, 'url_image', lb.url_image
#     )) AS list_b,
#     IF (la.deleted IS NULL,JSON_OBJECT(
#     'id', la.id, 'namedest', la.name_delivery, 'city', la.city, 'district', la.district,
#     'state', la.uf, 'zipcode', la.cep, 'street', la.road, 'number', la.number_home
#     ), NULL) AS main_add,
#     JSON_ARRAYAGG(JSON_OBJECT('id', c.id, 'name_carrie', c.name_carrier, 'price', 15.65,'toDate', 6)) AS shipping_company
#     FROM (SELECT p.id, o.id AS opt_id, b.quantity, s.size, o.price, o.discount, p.title, ctg.category_name, cl.color, cl.color_name, pi.url_image, b.user_id
#     FROM bag AS b
#     INNER JOIN sizes AS s ON s.id = b.sizes_id
#     INNER JOIN options_product AS o ON o.id = b.option_product_id
#     INNER JOIN colors AS cl ON cl.id = o.colors_id
#     INNER JOIN products AS p ON p.id = o.products_id
#     INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id
#     INNER JOIN products_images AS pi ON pi.option_id = o.id
#     WHERE b.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1)
#     AND b.orders_id IS NULL GROUP BY o.id, s.id) AS lb,
#     (SELECT DISTINCT ad.id, ad.name_delivery, ad.city, ad.district, ad.uf, ad.cep, ad.road, ad.number_home, ad.deleted
#     FROM user_address AS ad
#     WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1) AND main = 1 LIMIT 1) AS la,
#     (SELECT id, name_carrier FROM carrier) AS c"""


q_bag_update_quantity = """UPDATE bag SET quantity = %(quantity)s WHERE 
    user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND option_product_id = %(product_option)s 
    AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s)"""


q_bag_delete_item = """DELETE FROM bag WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND option_product_id = %(product_option)s 
    AND sizes_id = (SELECT id FROM sizes WHERE size = %(size)s)"""
