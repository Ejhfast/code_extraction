# What's equivalent to Django's auto_now, auto_now_add in SQLAlchemy?
Column('created_on', DateTime, default=datetime.datetime.now)
