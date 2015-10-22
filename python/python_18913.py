# Postgresql: How to delete rows from table constrained by date?
cursor.execute('DELETE FROM datatable WHERE date &lt; %s', [datetime.date(2012, 1, 1)])
