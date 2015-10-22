# Python SQLite3 How to extract specific tables only
for tablename in cur.execute('SELECT name FROM sqlite_master WHERE type="table";'):
    if tablename[0].startswith('conn_'):
        execute_some_query_using_this_table()
