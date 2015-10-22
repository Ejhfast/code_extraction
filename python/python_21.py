# How do I copy a file to a remote server in python using scp or ssh?
import os
os.system("scp FILE USER@SERVER:PATH")
#e.g. os.system("scp foo.bar joe@srvr.net:/path/to/foo.bar")
