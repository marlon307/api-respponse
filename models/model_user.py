class qUser:
    def q_register_user():
        return "INSERT INTO user (id_user, name, email, password, user_token) VALUES (%(id_user)s, %(name)s, %(email)s, %(password)s,%(user_token)s)"

    def q_login_user():
        return "SELECT id_user, name, email, password, admin FROM user WHERE (email) = (%(email)s)"

    def q_request_update_token():
        return "UPDATE user SET user_token = %(key)s WHERE (email) = %(email)s"

    def q_select_emailuser():
        return "SELECT email, id_user FROM user WHERE email = %(email)s AND confirm_acc = %(confirm_acc)s"

    def q_select_user_token():
        return "SELECT user_token FROM user WHERE email = %(email)s AND confirm_acc = %(confirm_acc)s"

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
        return (
            "SELECT u.name, u.email, u.birthday, u.cpf_cnpj, u.gender_id, "
            "JSON_ARRAYAGG(JSON_OBJECT("
            "'id', tel.id,"
            "'phone', tel.number_phone"
            ") ) AS telephones FROM user AS u "
            "LEFT JOIN telephones AS tel "
            "ON tel.user_id = u.id "
            "WHERE u.id_user = %(user_id)s "
            "GROUP BY u.id"
        )


# SELECT CONCAT(
#     '[',
#     GROUP_CONCAT(JSON_OBJECT('name', name, 'phone', phone)),
#     ']'
# )
# FROM person;
