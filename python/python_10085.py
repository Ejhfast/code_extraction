# parameterized queries in oursql
c.execute("""SELECT * FROM records WHERE id = %(id)s""", {"id": 2})
