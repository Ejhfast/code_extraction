# loading another program that takes in a textfile in a program subprocess
cmd = 'ping 192.168.1.1'
output = subprocess.check_output(cmd.split())
