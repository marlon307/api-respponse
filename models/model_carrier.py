q_isert_carries = """INSERT IGNORE INTO carrier (id, name_carrier, service, picture) VALUES (%(id)s, %(name)s, %(service)s, %(picture)s)"""

q_insert_sizes = """INSERT IGNORE INTO carrier_sizes (carrier_id, weight_max, weight_min, width_max, width_min, 
height_max, height_min, length_max, length_min, diameter_max, diameter_min, sum, type)
VALUES (%(carrier_id)s, %(weight_max)s, %(weight_min)s, %(width_max)s, %(width_min)s, 
%(height_max)s, %(height_min)s, %(length_max)s, %(length_min)s, %(diameter_max)s, %(diameter_min)s, %(sum)s, %(type)s)"""

q_update_value_shipping = """UPDATE orders SET delivery_value = %(delivery_value)s
        WHERE user_id = (SELECT id FROM user WHERE id_user = %(p_userid)s LIMIT 1)
        AND id = %(order_id)s;"""
