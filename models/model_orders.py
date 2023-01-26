q_get_orders = """SELECT o.id, date_order, s.status 
    FROM orders AS o 
    INNER JOIN status AS s ON s.id = o.status_id 
    WHERE user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) 
    ORDER BY o.id DESC"""

q_get_order_id = """SELECT o.id, o.status_id, o.date_order, o.value_order, pay.name AS payment, 
    JSON_OBJECT('name_delivery', uadd.name_delivery, 'city', uadd.city, 'district', uadd.district, 
    'uf', uadd.state, 'zipcode', uadd.zipcode, 'number_home', uadd.number_home, 'road', uadd.street) AS address, 
    JSON_OBJECT('name_carrier', crr.name_carrier, 'code', o.tracking_code, 'delivery_value', o.delivery_value) AS carrier, 
    JSON_ARRAYAGG(JSON_OBJECT( 
    'title', p.title, 'category_name', ctg.category_name, 'id', p.id, 
    'size', sz.size, 'quantity', b.quantity, 
    'url_image', img.url_image, 'color', cl.color, 
    'color_name', cl.color_name, 'price', b.price 
    )) AS list_products 
    FROM orders AS o 
    INNER JOIN user_address AS uadd ON uadd.id = o.address_id 
    INNER JOIN carrier AS crr ON crr.id = o.carrier_id 
    INNER JOIN bag AS b ON b.orders_id = o.id 
    INNER JOIN options_product AS op ON op.id = b.option_product_id 
    INNER JOIN products AS p ON p.id = op.products_id 
    INNER JOIN categorys AS ctg ON ctg.id = p.categorys_id 
    INNER JOIN sizes AS sz ON sz.id = b.sizes_id 
    INNER JOIN payment AS pay ON pay.id = o.payment_id 
    INNER JOIN LATERAL 
    (SELECT option_id, url_image FROM products_images AS im WHERE im.option_id = op.id LIMIT 1) 
    AS img ON img.option_id = b.option_product_id 
    INNER JOIN colors AS cl ON cl.id = op.colors_id 
    WHERE o.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) AND o.id = %(order_id)s"""

q_order_seller = """SELECT DISTINCT o.id, s.status, o.date_order 
    FROM orders AS o 
    INNER JOIN status AS s ON s.id = o.status_id 
    INNER JOIN bag AS b ON b.orders_id = o.id 
    INNER JOIN options_product AS op On op.id = b.option_product_id 
    INNER JOIN products AS p ON p.id = op.products_id 
    WHERE p.user_id = (SELECT id FROM user WHERE id_user =%(id_user)s) AND s.id = %(status_id)s"""

q_panel_order_seller = """SELECT s.status, COUNT(*) AS 'quantity' 
FROM orders AS o
INNER JOIN status AS s ON s.id = o.status_id
INNER JOIN bag AS b ON orders_id = o.id
INNER JOIN options_product AS op ON op.id = b.option_product_id
INNER JOIN products AS p ON p.id = op.products_id
WHERE p.user_id = (SELECT id FROM user WHERE id_user = %(id_user)s)  
GROUP BY o.status_id 
ORDER BY s.id ASC"""

q_products_seller = """SELECT COUNT(*) AS 'quantity' FROM products WHERE user_id = (SELECT id FROM user WHERE id_user = %(id_user)s)"""

q_update_payment_order = """UPDATE orders SET transaction_id = %s WHERE id = %s"""

q_update_payment_order_status = """
UPDATE orders SET status_id = 2 WHERE transaction_id = %s"""
