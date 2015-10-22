# Read database entries from mysql in the form of dictionary in python
db_conn = mdb.connect(
    host="localhost", user="username", passwd="password", db="db_name",
    charset='utf8', cursorclass=mdb.cursors.DictCursor)
