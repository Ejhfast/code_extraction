# Python: use mysqldb to import a MySQL table as a dictionary?
import MySQLdb.cursors
MySQLdb.connect(host='...', cursorclass=MySQLdb.cursors.DictCursor)
