# MySQLdb executemany using a list as input?
params = [(str(keywords[i]), date, time, position[i]) for i in range(20)]
