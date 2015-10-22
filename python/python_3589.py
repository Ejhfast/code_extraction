# querying relation does not give back related object in sqlalchemy
token = Session.query(AuthToken).options(eagerload('user')).filter(...).one()
user = token.user
