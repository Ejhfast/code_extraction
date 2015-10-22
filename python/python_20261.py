# Read things out of database WHERE 'id'=
query = "SELECT FRwoord, NLwoord FROM unite8app1 WHERE id=%s"
cursor.execute(query, (willekeurig,))
