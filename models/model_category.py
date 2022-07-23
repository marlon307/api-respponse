class qCategory:
    def q_insert_category():
        return (
            "INSERT INTO categorys (url_image, category_name, sub_title, path, color)"
            "VALUES (%(c_image)s, %(c_name)s, %(c_title)s, %(c_path)s, %(c_color)s)"
        )
