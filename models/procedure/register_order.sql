CREATE DEFINER=`root`@`localhost` PROCEDURE `register_order`(p_userid CHAR(36), p_addressid INT, p_carriesid INT, method_pay VARCHAR(100), delivery_value FLOAT)
BEGIN
		DECLARE iduser INT;
		DECLARE idaddres INT;
    DECLARE price FLOAT;
    DECLARE quantityvols INT;
    DECLARE idorder INT;
    DECLARE paymentid INT;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        
		GET DIAGNOSTICS CONDITION 1
		@p1 = RETURNED_SQLSTATE, @p2 = MESSAGE_TEXT;
        
        SELECT op.products_id AS product_id, opsz.options_product_id, @p1 as RETURNED_SQLSTATE, @p2 as MESSAGE_TEXT FROM bag AS b 
			INNER JOIN options_product_has_sizes AS opsz ON opsz.options_product_id = b.option_product_id AND opsz.sizes_id = b.sizes_id
            INNER JOIN options_product AS op ON op.id = opsz.options_product_id
			WHERE b.user_id = iduser AND b.orders_id IS NULL LIMIT 1;
    END; 
    
    SET iduser = (SELECT id FROM user WHERE id_user = p_userid);
    SET idaddres = (SELECT id FROM user_address WHERE user_id = iduser AND id = p_addressid);
    SET price = (SELECT SUM(b.quantity * op.price) FROM bag AS b
				 INNER JOIN options_product AS op ON op.id = b.option_product_id
				 WHERE b.user_id = iduser AND b.orders_id IS NULL);
		SET quantityvols = (SELECT SUM(quantity) FROM bag AS b WHERE b.user_id = iduser AND b.orders_id IS NULL); 
    SET paymentid = (SELECT id FROM payment WHERE type_id = method_pay LIMIT 1);
    
    IF price IS NOT NULL AND idaddres IS NOT NULL AND iduser IS NOT NULL THEN
		START TRANSACTION;
			INSERT INTO orders (user_id, address_id, carrier_id, status_id, value_order, quantity_vol, payment_id, delivery_value) 
			VALUES (iduser, idaddres, p_carriesid, 1, price, quantityvols, paymentid, delivery_value);
			SET idorder = (SELECT LAST_INSERT_ID() FROM orders AS o WHERE o.user_id = iduser LIMIT 1);
			
			UPDATE bag AS b 
			INNER JOIN options_product_has_sizes AS opsz ON opsz.options_product_id = b.option_product_id AND opsz.sizes_id = b.sizes_id
            INNER JOIN options_product AS op ON op.id = b.option_product_id
			SET b.orders_id = idorder, opsz.quantity = opsz.quantity - b.quantity, b.price = op.price 
			WHERE b.user_id = iduser AND b.orders_id IS NULL;
		COMMIT;
        
		SELECT idorder AS 'number_order', price + delivery_value AS 'price', u.email, u.cpf_cnpj, u.name, ad.city, ad.* FROM user AS u
        INNER JOIN user_address AS ad ON user_id = iduser AND ad.id = idaddres
        WHERE u.id = iduser;
        
	ELSE
		SELECT '400 - Não possui informações o suficiente para registrar um pedido.' AS MSG;
        ROLLBACK;
	END IF;
END
