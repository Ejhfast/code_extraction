# Multiple executions using MySQLdb
from contextlib import closing
with closing( conn.cursor() ) as cursor:
    cursor.execute("INSERT INTO...")
