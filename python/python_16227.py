# SQLAlchemy User Defined Function Error
myfunc = select([column('x'), column('y')]).select_from(func.myfunction())
session.execute(myfunc).fetchall()
