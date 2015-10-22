# Python Regex - Escaping
In [68]: re.match('((?P&lt;user&gt;.*):)((?P&lt;pass&gt;.*)@)((?P&lt;host&gt;.*)/)((?P&lt;db&gt;.*))', "username:p@ssword@host/data").groupdict()
Out[68]: {'db': 'data', 'host': 'host', 'pass': 'p@ssword', 'user': 'username'}
