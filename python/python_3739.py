# Parameterizing 'SELECT IN (...)' queries
query = 'select * from table where key in (%s)' % ','.join('?' * len(serials))
c.execute(query, serials)
