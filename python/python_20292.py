# Make SQLAlchemy query by list case insensitive
session.query(datamodel).filter(func.lower(datamodel.fruitname).in_(fruits)).all()
