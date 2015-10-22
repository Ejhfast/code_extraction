# python - does cx_Oracle allow you to force all columns to be cx_Oracle.STRING?
r = cursor.execute("select to_char( thetime, 'DD-MON-RR HH24.MI.SSXFF' ) from my_table")
