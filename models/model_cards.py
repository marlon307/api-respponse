q_insert_card = """INSERT INTO cards (user_id, titular_name, number, expiration_date, flag, cpf_cnpj, birthday) 
    VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1),
    %(c_name)s, %(c_number)s, %(c_exp)s, %(c_flag)s, %(c_cpf_cnpj)s, %(c_birthday)s)"""
