# SQLAlchemy: Select count of related many-to-many elements
cnt = db.func.count(db.distinct(Content.id))
