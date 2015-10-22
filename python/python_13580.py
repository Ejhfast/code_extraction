# how to copy os.system('cat /var/log/dmesg') to a variable
with open('/var/log/dmesg') as logf:
    log = logf.read()
print(log)
