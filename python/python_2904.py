# Way to query database with SQLAlchemy where a date is a particular day of the week?
query.filter("strftime('%w', access_date) = :dow").params(dow=0).all()
