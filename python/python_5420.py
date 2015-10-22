# SQLite Python AND statement not working
sql_statement = """SELECT * FROM points WHERE strftime('%s', checkintime) == %s AND strftime('%s', checkintime) == %s""" % ('%H', time, '%w', day)
