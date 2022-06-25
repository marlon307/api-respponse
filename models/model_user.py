class qUser:
    def q_register_user():
        return "INSERT INTO user (id_user, name, email, password) VALUES (%(id_user)s, %(name)s, %(email)s, %(password)s)"

    def q_login_user():
        return "SELECT id_user, name, email, password FROM user WHERE (email) = (%(email)s)"
