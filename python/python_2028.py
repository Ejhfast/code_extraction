# Map only certain parts of the class to a database using SQLAlchemy?
mapper(User, users_table, include_properties=['user_id', 'user_name'])
