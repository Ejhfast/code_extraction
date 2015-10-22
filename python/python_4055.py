# is there a way to do a insert an request the scope_identity() using pyodbc to sql server 2005
cur = con.execute(
         "insert into sometable OUTPUT INSERTED.idcolumn values('something')"
         )
