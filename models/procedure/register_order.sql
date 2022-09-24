CREATE DEFINER=`root`@`localhost` PROCEDURE `register_order`(
p_userid CHAR(36), p_addressid INT, p_carriesid INT, p_deliveryvalue FLOAT)
BEGIN
	DECLARE iduser INT;
	DECLARE idaddres INT;
    DECLARE price INT;
    DECLARE quantityvols INT;
    DECLARE idorder INT;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SHOW ERRORS;  -- this is the only one which you need
        ROLLBACK;   
    END; 
    
    SET iduser = (SELECT id FROM user WHERE id_user = p_userid);
    SET idaddres = (SELECT id FROM user_address WHERE user_id = iduser AND id = p_addressid);
    SET price = (SELECT SUM(op.price) FROM bag AS b
				 INNER JOIN options_product AS op ON op.id = b.option_product_id
				 WHERE b.user_id = iduser AND b.orders_id IS NULL);
	SET quantityvols = (SELECT SUM(quantity) FROM bag AS b WHERE b.user_id = iduser AND b.orders_id IS NULL); 
    
    START TRANSACTION;
		INSERT INTO orders (user_id, address_id, carrier_id, status_id, value_order, quantity_vol, delivery_value) 
		VALUES (iduser, idaddres, p_carriesid, 1, price, quantityvols, p_deliveryvalue);
		SET idorder = (SELECT LAST_INSERT_ID() FROM orders AS o WHERE o.user_id = iduser LIMIT 1);
		
		UPDATE bag AS b 
		INNER JOIN options_product_has_sizes AS opsz ON opsz.options_product_id = b.option_product_id AND opsz.sizes_id = b.sizes_id
		SET b.orders_id = idorder, opsz.quantity = opsz.quantity - b.quantity 
		WHERE b.user_id = iduser AND b.orders_id IS NULL;
	COMMIT;
END
