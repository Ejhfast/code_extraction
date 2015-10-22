# Execute background process from django that can't be interrupted by the web server
os.system("echo '/usr/bin/python /(somewhere)/scripts/backup/testbackup.py' | at now")
