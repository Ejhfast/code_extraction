# TCP Socket file transfer
buff=''
while len(buff) &lt; 1024:
    buff += s.recv( 1024 - len(buff) )
