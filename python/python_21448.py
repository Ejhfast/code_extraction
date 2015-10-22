# How to do this Python subprocess call without using shell=True?
In [3]: shlex.split(s)
Out[3]: ['bash', '-c', 'shred -n 5 -uz /tmp/{*.txt,*.pdf,*.doc}']
