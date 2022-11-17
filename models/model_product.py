q_insert_product = """INSERT INTO products 
    (categorys_id, gender_id, user_id, title, warranty, details, specifications) 
    VALUES (%(categorys_id)s, %(gender_id)s, (SELECT id FROM respponse_db.user WHERE id_user = %(id_user)s), %(title)s, %(warranty)s, %(details)s, %(specifications)s)"""

q_insert_product_option = """INSERT INTO options_product 
    (colors_id, price, discount, sku, products_id) 
    VALUES (%(colors_id)s, %(price)s, %(discount)s, %(sku)s, %(products_id)s)"""

q_insert_option_has_sizes = """INSERT INTO options_product_has_sizes 
    (options_product_id, sizes_id, quantity) 
    VALUES (%(options_product_id)s, %(sizes_id)s, %(quantity)s)"""

q_insert_image = """INSERT INTO products_images 
    (option_id, url_image, key_img, upload_id) 
    VALUES (%(option_id)s, %(url_image)s, %(key_img)s, %(upload_id)s)"""

q_list_prod = """SELECT JSON_ARRAYAGG(
JSON_OBJECT('id', ob_lp.id, 'title', ob_lp.title, 'category_name', ob_lp.category_name, 'color_list', ob_lp.color_list)
) AS list_product, 
JSON_ARRAYAGG(
JSON_OBJECT('ctgID', ctg.id, 'categoryName', ctg.category_name, 'path', ctg.path, 'color', ctg.color, 'sub_title', ctg.sub_title, 'imgCategory', ctg.url_image)
) AS categorys 
FROM 
(SELECT p.id, p.title, c.category_name, 
JSON_ARRAYAGG(JSON_OBJECT( 
'id', cl.id, 'price', op.price, 'discount', op.discount, 'url_image', i.url_image, 
'color_name', cl.color_name, 'color', cl.color 
)) AS color_list 
FROM products AS p 
INNER JOIN categorys AS c ON c.id = p.categorys_id 
INNER JOIN options_product AS op ON op.products_id = p.id 
INNER JOIN colors AS cl ON cl.id = op.colors_id 
INNER JOIN LATERAL 
(SELECT option_id, url_image FROM products_images AS im WHERE im.option_id = op.id GROUP BY option_id LIMIT 1) 
AS i ON i.option_id = op.id 
GROUP BY p.id 
LIMIT 20) AS ob_lp,
(SELECT * FROM categorys) AS ctg"""

q_get_product_id = """SELECT p.id, p.title, p.details, p.specifications, c.category_name, 
    JSON_ARRAYAGG(JSON_OBJECT('option_id', op.id, 'price', op.price, 'discount', op.discount, 'idc', cl.id, 'colorName', cl.color_name, 'color', cl.color)) AS list_options, 
    JSON_ARRAYAGG(JSON_OBJECT('option_id', opHs.options_product_id, s.size, opHs.quantity)) AS list_sizes, 
    JSON_ARRAYAGG(JSON_OBJECT('option_id', op.id, 'imgid', i.id, 'urlImg', i.url_image)) AS list_images 
    FROM products AS p 
    INNER JOIN categorys AS c ON c.id = p.categorys_id 
    INNER JOIN options_product AS op ON op.products_id = p.id 
    INNER JOIN colors AS cl ON cl.id = op.colors_id 
    INNER JOIN options_product_has_sizes AS opHs ON opHs.options_product_id = op.id 
    INNER JOIN sizes AS s ON s.id = opHs.sizes_id 
    INNER JOIN products_images AS i ON i.option_id = op.id 
    WHERE p.id = %(id)s 
    GROUP BY p.id"""
