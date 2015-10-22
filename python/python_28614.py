# Periodically outputting SQL table to a file
import subprocess
f=open('file.txt','w')
subprocess.call(['sqlite3', 'dbname.db', '-csv', 'select * from table'], stdout=f)
