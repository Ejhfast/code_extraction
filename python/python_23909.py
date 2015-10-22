# python how to know if subprocess is waiting for input
child = pexpect.spawn('my-process -v')
child.expect('Please enter your name:')
child.sendline(user_name)
