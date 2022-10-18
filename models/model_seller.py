q_list_options = (
    "SELECT list_colors.list_colors, list_categorys.list_ctg, list_gender.list_gender, list_sizes.list_sizes "
    "FROM "
    "(SELECT JSON_ARRAYAGG(JSON_OBJECT('id',  c.id, 'url_image',  c.url_image, 'category_name' , c.category_name, 'sub_title', c.sub_title, 'color', c.color)) AS list_ctg FROM categorys AS c) AS list_categorys, "
    "(SELECT JSON_ARRAYAGG(JSON_OBJECT('id',  c.id, 'color_name' , c.color_name, 'color', c.color)) AS list_colors FROM colors AS c) AS list_colors, "
    "(SELECT JSON_ARRAYAGG(JSON_OBJECT('id' , g.id, 'gender', g.gender, 'gender_name', g.name_gender)) AS list_gender FROM gender AS g) AS list_gender, "
    "(SELECT JSON_ARRAYAGG(JSON_OBJECT('id' , s.id, 'size', s.size)) AS list_sizes FROM sizes AS s) AS list_sizes"
)
