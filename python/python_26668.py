# Python odbc cursor: keeping persistent state after executing a query
string = 'dsn=hive/driver/path;mapred.reduce.tasks=100;....'
connection = pyodbc.connect(string, autocommit=True)
