# Python How to check for no return
result = commands.getoutput('diff a.txt b.txt')
if len(result) == 0:
   print 'Success'
