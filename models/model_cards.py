q_insert_card = """INSERT INTO cards (user_id, titular_name, number, expiration_date, flag, cpf, birthday) 
    VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1),
    %(c_name)s, %(c_number)s, %(c_exp)s, %(c_flag)s, %(c_cpf)s, %(c_birthday)s)"""
