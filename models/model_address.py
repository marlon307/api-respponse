class qAddress:
    def q_insert_address():
        return (
            "INSERT INTO respponse_db.user_address (user_id, name_delivery, city, district, uf, cep, road, number_home) "
            "VALUES ("
            "(SELECT id FROM respponse_db.user WHERE id_user = %(user_id)s),"
            "%(name_delivery)s, %(city)s, %(district)s, %(uf)s, %(cep)s, %(road)s, %(number_home)s)"
        )
