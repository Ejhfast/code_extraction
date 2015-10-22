# Set connection settings with Pyodbc + UnixODBC + FreeTDS
cnxn = pyodbc.connect("DSN=someDSN;UID=someUser;PWD=somePass;QuotedID=Yes;AnsiNPW=Yes")
