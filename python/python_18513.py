# SQLAlchemy query, join on relationship and order by count
db.session.query(Post, db.func.count(Like.id)).outerjoin(Like).group_by(Post.id)
