# How to override NULL value from aggregate query using MySQLdb module in python?
min_date = cur.fetchone()[0]
min_date = min_date if min_date is not None else default_value
