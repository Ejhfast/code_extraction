# perform echo xyz | ssh ... with python
shell_cmd = 'ls -l | grep LOG &gt; log_list.txt'
child = pexpect.spawn('/bin/bash', ['-c', shell_cmd])
child.expect(pexpect.EOF)
