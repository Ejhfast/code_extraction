# Sqlalchemy get last X rows in order
query = users.select().order_by(users.c.id.desc()).limit(5)
