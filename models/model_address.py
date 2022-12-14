q_insert_address = """INSERT INTO user_address (user_id, name_delivery, city, district, uf, cep, road, number_home) 
    VALUES (
    (SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1),
    %(namedest)s, %(city)s, %(district)s, %(state)s, %(zipcode)s, %(street)s, %(number)s)"""

q_get_address = """SELECT ad.id, ad.name_delivery, ad.city, ad.district, ad.state, ad.zipcode, ad.street, ad.number_home 
    FROM user_address AS ad 
    WHERE ad.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND ad.deleted IS NULL"""


q_delete_address = """UPDATE user_address AS ad 
    SET ad.deleted = %(delete_date)s 
    WHERE ad.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    AND ad.id = %(address_id)s 
    AND ad.deleted IS NULL"""
