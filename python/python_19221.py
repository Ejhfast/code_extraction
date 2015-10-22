# Dynamically query a subset of columns in sqlalchemy
columns = ['id', 'name']
print session.query(select(from_obj=User, columns=columns)).all()
