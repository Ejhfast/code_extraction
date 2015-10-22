# Using WHERE query for a datetime field with pyodbc and Excel.
cursor.execute('SELECT [Data/time] FROM [data_5min$] WHERE [Data/time] = #1/1/2010#')
