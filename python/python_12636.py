# Write unicode gif to file in python
utf8data = data.encode('UTF-8')
open('file.gif', 'w').write(utf8data)
