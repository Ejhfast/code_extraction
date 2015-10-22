# "Unclosed quotation mark" when connecting with pypyodbc
conn = pypyodbc.connect("DRIVER={SQL Server};server='sqldev\\master',Database='risk',TrustedConnection=yes")
cur = conn.cursor()
