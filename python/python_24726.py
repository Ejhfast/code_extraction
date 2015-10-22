# pandas.read_sql 'Invalid Cursor state'
with ceODBC.connect(self.CONNECT_STR) as conn:
    result = pandas.read_sql(sql, conn)
