# Python UnicodeEncodeError
import MySQLdb
dbcon = MySQLdb.connect(user="root",db="twitter",use_unicode=True,charset='UTF8')
