# Python output to terminal during ssh login
child = pexpect.spawn('scp foo myname@host.example.com:.')
child.expect ('Password:')
child.sendline (mypassword)
