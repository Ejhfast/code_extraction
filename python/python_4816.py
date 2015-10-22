# using eval to programmatically define an SQLQuery q object
Users.select(getattr(Users.q, column)==value)
