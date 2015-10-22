# Read from keyboard non blocking mode because of sockets working, python
selectList = [sktTCP,sys.stdin]
(read, write, exc) =  select.select(selectList, [], [], 0 )
