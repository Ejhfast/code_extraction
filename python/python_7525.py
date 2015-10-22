# How to get SqlAlchemy Table to read "implicit" schema
t = Table(name, meta, autoload=True)#, autoload_with=engine)
