# Using a list to create columns on MySQL
query = "ALTER TABLE taula ADD %s VARCHAR(255)".format(x)
c.execute(query,())
