# instancemethod object is unsubscriptable for in_ method
a = session.query(table).filter(table.c.id.in_(['1', '2']))
