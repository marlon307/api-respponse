q_list_options = """SELECT list_colors.list_colors, list_categorys.list_ctg, 
list_gender.list_gender, list_sizes.list_sizes FROM 
    (SELECT JSON_ARRAYAGG(JSON_OBJECT('id',  c.id, 'url_image',  c.url_image, 'category_name' , c.category_name, 'sub_title', c.sub_title, 'color', c.color)) AS list_ctg FROM categorys AS c) AS list_categorys, 
    (SELECT JSON_ARRAYAGG(JSON_OBJECT('id',  c.id, 'color_name' , c.color_name, 'color', c.color)) AS list_colors FROM colors AS c) AS list_colors, 
    (SELECT JSON_ARRAYAGG(JSON_OBJECT('id' , g.id, 'gender', g.gender, 'gender_name', g.name_gender)) AS list_gender FROM gender AS g) AS list_gender, 
    (SELECT JSON_ARRAYAGG(JSON_OBJECT('id' , s.id, 'size', s.size)) AS list_sizes FROM sizes AS s) AS list_sizes"""


q_update_settings_seller = """UPDATE user 
    SET cnpj=%(cnpj)s, ie=%(ie)s, name_store=%(store_name)s, collect_address_id=%(address)s, obs=%(obs)s 
    WHERE id_user=%(id_user)s"""

q_insert_boxes_seller = """INSERT INTO box_seller (id, user_id, width, height, length, weight) 
VALUES (%(id)s, (SELECT id FROM user WHERE id_user=%(user_id)s), %(width)s, %(height)s, %(length)s, %(weight)s) 
ON DUPLICATE KEY UPDATE width=%(width)s, height=%(height)s, length=%(length)s, weight=%(weight)s"""

q_delete_boxes = """DELETE FROM box_seller 
WHERE user_id = (SELECT id FROM user WHERE id_user=%(user_id)s) AND id=%(idbox)s"""

q_select_seller_settings = """SELECT u.name_store AS store_name, u.cnpj, u.ie, u.email, u.obs, 
JSON_OBJECT('id', a.id, 'name_delivery', a.name_delivery, 'zipcode', a.zipcode, 'city', a.city,
'district', a.district, 'street', a.street, 'district', a.district, 'complement', a.complement,
'number_home', a.number_home, 'state', a.state) AS address,
COALESCE((SELECT JSON_ARRAYAGG(JSON_OBJECT('id', bs.id, 'width', bs.width, 'height', bs.height,
'length', bs.length, 'weight', bs.weight, 'vol', bs.vol))
FROM box_seller AS bs WHERE user_id = u.id)
, '[]') AS boxes FROM user AS u 
INNER JOIN user_address AS a ON a.id = u.collect_address_id 
WHERE id_user = %(id_user)s OR u.id = %(iduser)s GROUP BY u.id"""
