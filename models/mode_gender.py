class qGender:
    def q_insert_gender():
        return (
            "INSERT INTO gender (gender, name_gender)"
            "VALUES (%(g_initials)s, %(g_name)s)"
        )
