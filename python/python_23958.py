# How to copy a database with mysqldump and mysql in Python?
subprocess.Popen('mysqldump -h localhost -P 3306 -u -root mydb | mysql -h localhost -P 3306 -u root mydb2', shell=True)
