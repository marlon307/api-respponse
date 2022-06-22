from models.database import cursor, cnn


class User:
    def register_user(json):
        query = "INSERT INTO user (name, email, password) VALUES (%(name)s, %(email)s, %(password)s)"
        cursor.execute(query, json)
        cnn.commit()
        cursor.close()
        cnn.close()
