# Automated database restore from *.sql files
process = Popen('mysql %s -u%s' % (db, "root"), stdout=PIPE, stdin=PIPE, shell=True) output = process.communicate('source' + file)[0]
