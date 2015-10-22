# regexp fails for utf8 character matching, even when using re.UNICODE
GeoAlchemy ST_DWithin implementation
posts = db.session.query(Post).filter(func.ST_DWithin(Post.location, point, 10))
