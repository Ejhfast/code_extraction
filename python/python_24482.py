# TypeError when calling expect method of pexpect module in Python 3
# In Python 3, spawnu should be used to give str to stdout:
child = pexpect.spawnu('some_command')
child.logfile = sys.stdout
