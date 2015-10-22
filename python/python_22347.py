# regular expression to recognize 'x:...y:...z:...' in python
re.compile('\w+:[^:]*?(?=\w+:|$)')
