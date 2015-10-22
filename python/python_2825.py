# Accessing a XAMPP mysql via Python
db=MySQLdb.connect(user="root",passwd="",db="my_db",unix_socket="/opt/lampp/var/mysql/mysql.sock")
