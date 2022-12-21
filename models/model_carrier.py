q_isert_carries = """INSERT IGNORE INTO carrier (id, name_carrier, service, picture) VALUES (%(id)s, %(name)s, %(service)s, %(picture)s)"""

q_update_value_shipping = """UPDATE orders SET delivery_value = %(delivery_value)s
        WHERE user_id = (SELECT id FROM user WHERE id_user = %(p_userid)s LIMIT 1)
        AND id = %(order_id)s;"""
