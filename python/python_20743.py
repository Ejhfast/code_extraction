# How can I do this in SQLAlchemy?
session().query(AnotherModel).join(Entity).filter(Entity.is_published)
