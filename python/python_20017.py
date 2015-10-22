# python pexpect: SSHing then updating the date
self.sendline()       #line 134
time.sleep(0.5)       #line 135
self.read_nonblocking(size=10000,timeout=1) # GAS: Clear out the cache before getting the prompt
