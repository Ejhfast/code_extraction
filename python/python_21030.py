# Using an SQL expression to insert data with SQLAlchemy (and MySQL)
ins = table.insert().values(a=None, b=2, c=func.now())
engine.execute(ins)
