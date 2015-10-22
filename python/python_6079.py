# Python: Checking if field exists in table
if "select count(*) from scan where prefix = ? and code_id = ? and ..." == 0:
    execute("insert into scan....")
