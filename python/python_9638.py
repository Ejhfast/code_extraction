# Python2 setting time error
command = ['date', '-s"' + time.ctime(val) + '"']
subprocess.call(command)
