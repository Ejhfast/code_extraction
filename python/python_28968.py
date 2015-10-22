# Python: PSQL: Generate list from query
li = [item[0] for item in cur.fetchall()]
print li
'['Bakkerij.Device1.DB100INT0', 'Bakkerij.Device1.DB100INT4', 'Bakkerij.Device1.DB100INT8']'
