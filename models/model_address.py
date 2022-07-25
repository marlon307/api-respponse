class qAddress:
    def q_insert_address():
        return (
            "INSERT INTO user_address (user_id, name_delivery, city, district, uf, cep, road, number_home) "
            "VALUES ("
            "(SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1),"
            "%(name_delivery)s, %(city)s, %(district)s, %(uf)s, %(cep)s, %(road)s, %(number_home)s)"
        )
