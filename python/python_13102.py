# Filter by exact date after receiving webapp2 request on Python GAE
custQuery = db.Query(Customer)
birthdate = datetime.strptime(q,"%Y-%m-%d").date()
custQuery.filter('birthdate = ',birthdate)
