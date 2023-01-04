q_insert_category = """INSERT INTO categorys (url_image, category_name, sub_title, path, color)
    VALUES (%(c_image)s, %(c_name)s, %(c_title)s, %(c_path)s, %(c_color)s)"""

q_select_categorys = "SELECT url_image, category_name, path, color FROM categorys"

q_list_prod_category = """SELECT p.id, p.title, c.category_name, g.name_gender, 
JSON_ARRAYAGG(JSON_OBJECT( 'id', cl.id, 'sizes', s.sizes, 
'price', op.price, 'discount', op.discount, 'url_image', i.url_image, 
'color_name', cl.color_name, 'color', cl.color
)) AS color_list 
FROM products AS p 
INNER JOIN gender AS g ON g.id = p.gender_id 
INNER JOIN categorys AS c ON c.id = p.categorys_id 
INNER JOIN options_product AS op ON op.products_id = p.id 
INNER JOIN colors AS cl ON cl.id = op.colors_id 
INNER JOIN LATERAL (
SELECT hs.options_product_id, JSON_ARRAYAGG(s.size) AS sizes FROM options_product_has_sizes AS hs 
INNER JOIN sizes AS s ON s.id = hs.sizes_id 
WHERE hs.options_product_id = op.id 
AND hs.quantity > 0 
GROUP BY hs.options_product_id
) AS s 
INNER JOIN LATERAL 
(SELECT DISTINCT option_id, url_image FROM products_images AS im 
WHERE im.option_id = op.id LIMIT 1) AS i ON i.option_id = op.id 
WHERE c.category_name = %(ctg_name)s 
GROUP BY p.id"""
