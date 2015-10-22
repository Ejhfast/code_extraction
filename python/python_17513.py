# Make a stream read() blocking
flag = fcntl.fcntl(MyStream.fileno(), fcntl.F_GETFL)
fcntl.fcntl(MyStream.fileno(), fcntl.F_SETFL, flag &amp; ~os.O_NONBLOCK)
