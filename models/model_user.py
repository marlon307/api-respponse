class qUser:
    def q_register_user():
        return "INSERT INTO user (name, email, password) VALUES (%(name)s, %(email)s, %(password)s)"

    def q_login_user():
        return "SELECT name, email FROM user WHERE (email, password) = (%(email)s, %(password)s)"
