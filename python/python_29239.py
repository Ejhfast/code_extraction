# Running sqoop using python subprocess can't recognize the arguments
call(["/usr/local/sqoop/bin/sqoop","export","--connect", "jdbc:mysql://localhost/temp","--table", "table1" ,"--export-dir", "/user/data/input" ,"--username", "root"])
