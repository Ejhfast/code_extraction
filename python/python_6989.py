# Subtract SQL DATETIME from datetime.now() in Python
start = time.strptime('2012-08-26 13:00:00', '%Y-%m-%d %H:%M:%S')
start = datetime.datetime(*start[:6])
