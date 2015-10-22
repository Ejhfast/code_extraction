# Calling a stored procedure python
conn = pyodbc.connect(driver = '{SQL Server Native Client 10.0}', server = '(local)',            database = 'Inventory', uid = 'sa', pwd = 'p@$$w0rd123',autocommit=True)
