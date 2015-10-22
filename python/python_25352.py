# filter with more than one value on flask-sqlalchemy
query = Notification.query.filter(Notification.id.in_(my_list)).all()
