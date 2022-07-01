class qUser:
    def q_register_user():
        return "INSERT INTO user (id_user, name, email, password) VALUES (%(id_user)s, %(name)s, %(email)s, %(password)s)"

    def q_login_user():
        return "SELECT id_user, name, email, password FROM user WHERE (email) = (%(email)s)"

    def q_request_rest_psw():
        return "UPDATE user SET key_resetpsw = %(key)s WHERE (email) = %(email)s"

    def q_select_emailuser():
        return "SELECT email, id_user FROM user WHERE email = %(email)s"

    def q_select_k_userpsw():
        return "SELECT key_resetpsw FROM user WHERE email = %(email)s"

    def q_update_psw_user():
        return (
            "UPDATE user SET "
            "password=%(password)s, key_resetpsw=%(key_resetpsw)s "
            "WHERE id_user=%(id_user)s AND email=%(email)s"
        )
