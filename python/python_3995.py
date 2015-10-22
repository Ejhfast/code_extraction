# Python - run external script
with file('a.py','rU') as f:
  co=compile(f.read(),'foobar','exec')
  exec co in {'__name__':'__main__'}
