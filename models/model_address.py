class qAddress:
    def q_insert_address():
        return (
            "INSERT INTO user_address (user_id, name_delivery, city, district, uf, cep, road, number_home) "
            "VALUES ("
            "(SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1),"
            "%(name_delivery)s, %(city)s, %(district)s, %(uf)s, %(cep)s, %(road)s, %(number_home)s)"
        )

    def q_get_address():
        return (
            "SELECT ad.id, ad.name_delivery, ad.city, ad.district, ad.uf, ad.cep, ad.road, ad.number_home "
            "FROM user_address AS ad "
            "WHERE ad.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
            "AND ad.deleted IS NULL"
        )

    def q_delete_address():
        return (
            "UPDATE user_address AS ad "
            "SET ad.deleted = %(delete_date)s "
            "WHERE ad.user_id = (SELECT id FROM user WHERE id_user = %(user_id)s) "
            "AND ad.id = %(address_id)s "
            "AND ad.deleted IS NULL"
        )
