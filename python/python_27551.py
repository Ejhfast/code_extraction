# Cx_Oracle.DatabaseError: ORA-00984: column not allowed here
cur.execute('INSERT INTO NONMODEL_CAT_HAZARD (LONGITUDE,LATITUDE,STATE,COUNTRY) VALUES (\''+str(long)+'\',\''+str(lat)+'\',\''+str(state)+'\',\''+str(cty)+'\')')
