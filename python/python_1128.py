# SQLAlchemy: relation in mappers compile result of function rather than calling the function when the relation is queried
and_(photo_content_table.c.photoId == photo_table.c.id, photo_content_table.c.locale == get_lang)
