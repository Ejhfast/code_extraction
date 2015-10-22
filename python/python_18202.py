# How can I send single ssh command to get result string with pexpect?
p = pexpect.spawn('ssh  %s@%s ls'%(un,ip), timeout)
print(p.read())
