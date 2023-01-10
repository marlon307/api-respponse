q_register_user = """INSERT INTO user (id_user, name, email, password, user_token) VALUES (%(id_user)s, %(name)s, %(email)s, %(password)s,%(user_token)s)"""

q_login_user = """SELECT id_user, name, email, password, admin FROM user 
WHERE (email) = (%(email)s)"""

q_request_update_token = """UPDATE user SET user_token = %(key)s 
WHERE (email) = %(email)s"""

q_select_emailuser = "SELECT email, id_user, name FROM user WHERE email = %(email)s"

q_select_user_token = "SELECT user_token FROM user WHERE email = %(email)s"

q_update_active_acc = """UPDATE user SET 
    confirm_acc=true, date_confirm_acc=%(date)s, user_token=%(user_token)s 
    WHERE id_user=%(id_user)s AND email=%(email)s"""

q_update_psw_user = """UPDATE user SET 
    password=%(password)s, user_token=%(user_token)s 
    WHERE id_user=%(id_user)s AND email=%(email)s"""

q_select_info_user = """SELECT name, email, birthday, cpf, gender_id, tel, cel 
FROM user WHERE id_user = %(user_id)s"""

q_update_user = """UPDATE user SET name=%(name)s, birthday=%(date)s, cpf=%(doc)s, gender_id=%(gender)s, tel=%(tel)s, cel=%(cel)s WHERE id_user=%(id_user)s"""
