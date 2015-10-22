# Pandas write_frame deletes sqlite table
pd_sql.uquery("DELETE FROM mytable", conn)
pd_sql.write_frame(d, 'mytable', conn, if_exists='append')
