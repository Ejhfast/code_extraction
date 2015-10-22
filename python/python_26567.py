# cx_Oracle: ORA-00922: missing or invalid option for alter session command
query = "alter session set \"_use_nosegment_indexes\" = true"
dbcursor.execute(query)
