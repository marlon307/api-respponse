class qUser:
    def q_register_user():
        return "INSERT INTO user (id_user, name, email, password, user_token) VALUES (%(id_user)s, %(name)s, %(email)s, %(password)s,%(user_token)s)"

    def q_login_user():
        return "SELECT id_user, name, email, password, admin FROM user WHERE (email) = (%(email)s)"

    def q_request_update_token():
        return "UPDATE user SET user_token = %(key)s WHERE (email) = %(email)s"

    def q_select_emailuser():
        return "SELECT email, id_user, name FROM user WHERE email = %(email)s AND confirm_acc = False"

    def q_select_user_token():
        return (
            "SELECT user_token FROM user WHERE email = %(email)s"
        )

    def q_update_active_acc():
        return (
            "UPDATE user SET "
            "confirm_acc=true, date_confirm_acc=%(date)s, user_token=%(user_token)s "
            "WHERE id_user=%(id_user)s AND email=%(email)s"
        )

    def q_update_psw_user():
        return (
            "UPDATE user SET "
            "password=%(password)s, user_token=%(user_token)s "
            "WHERE id_user=%(id_user)s AND email=%(email)s"
        )

    def q_select_info_user():
        return "SELECT name, email, birthday, cpf_cnpj, gender_id, tel, cel FROM user WHERE id_user = %(user_id)s"

    def q_update_user():
        return "UPDATE user SET name=%(name)s, birthday=%(date)s, cpf_cnpj=%(doc)s, gender_id=%(gender)s, tel=%(tel)s, cel=%(cel)s WHERE id_user=%(u_id)s"
