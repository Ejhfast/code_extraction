# sqlalchemy database table is locked
dealer = list(dealers.select().order_by(asc(dealers.c.id)).execute())
