# How to declared one-to-many if there are 2 fields for a same foreign key
user = relation('User', backref='articles', primaryjoin="Article.user_id==User.id")
