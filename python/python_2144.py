# SQLAlchemy: a better way for update with declarative?
session.query(User).filter_by(id=123).update({"name": u"Bob Marley"})
