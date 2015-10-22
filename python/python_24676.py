# Python os.popen and unicode
for line in os.popen('dir'):
      print(line.rstrip().encode('UTF-8')) # as utf8 is a universal encoding i use it you can use another too
