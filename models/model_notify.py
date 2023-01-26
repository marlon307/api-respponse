q_info_payment = """SELECT o.id AS 'number_order', o.value_order AS 'price', o.carrier_id, 
ad.name_delivery, ad.district, ad.state, ad.zipcode, ad.street, ad.number_home, ad.complement, ad.city, ad.obs, u.email, u.cpf, u.name, u.id AS 'id_user' 
FROM orders AS o 
INNER JOIN user_address AS ad ON ad.id = o.address_id 
INNER JOIN user AS u ON u.id = o.user_id 
WHERE transaction_id = %(id_payment)s"""


q_update_status = """UPDATE orders
SET status_id = 2
WHERE transaction_id = %(id_payment)s"""


q_update_tag = """UPDATE orders
SET tag = %(id_tag)s
WHERE transaction_id = %(id_payment)s"""
