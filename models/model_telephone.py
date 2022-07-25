class qTelephone:
    def q_insert_telephone():
        return (
            "INSERT INTO telephones (user_id, number_phone) "
            "VALUES ((SELECT id FROM user WHERE id_user = %(user_id)s LIMIT 1),"
            "%(n_phone)s)"
        )
