# Encode a dataframe after in import in sql
cnxn = pyodbc.connect('DRIVER={Teradata};DBCNAME=PRD;UID=*;PWD=*;QUIETMODE=YES;',
                       unicode_results=True)
