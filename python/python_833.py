# SQLAlchemy - Trying Eager loading.. Attribute Error
query = session.query(Zipcode).options(eagerload('zipcode')).filter(Zipcode.state.in_(['NH', 'ME'])).all()
