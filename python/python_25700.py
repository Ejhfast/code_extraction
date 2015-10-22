# Make a relationship between two tables though another
session.query(Listing).join(Property).join(Condominium).filter(Condominium.id=123)
