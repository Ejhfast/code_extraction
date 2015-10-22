# how do I read everything currently in a subprocess.stdout pipe and then return?
import fcntl, os
fcntl.fcntl(your_process.stdout, fcntl.F_SETFL, os.O_NONBLOCK)
