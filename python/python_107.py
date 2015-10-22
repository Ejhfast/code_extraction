# How to add an automatic filter to a relation with SQLAlchemy?
mapper(Something, select([sometable], sometable.c.deleted == False))
