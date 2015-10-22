# How to reduce number of connections using SQLAlchemy + postgreSQL?
engine = create_engine('postgresql://me@localhost/mydb',
                   pool_size=20, max_overflow=0)
