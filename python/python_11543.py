# Is there any way I can use 'nmap' port scanner, to generate and output result on my Django App
pout,perr = subprocess.Popen(['nmap', '192.168.1.2', '-oX', '-'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
