# SQLite returns Unicode buffer that cannot be converted to usable strings
print str(row[0]).decode('utf-16le')
