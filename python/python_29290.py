# Get a list of values of one column from the results of a query
emails = [r.email for u in db.session.query(my_table.c.email).filter_by(name=name).distinct()]
