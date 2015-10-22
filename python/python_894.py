# passing ctrl+z to pexpect
p = pexpect.spawn(your_cmd_here)
p.sendcontrol('z')
