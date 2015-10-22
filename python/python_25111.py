# Read hex characters and convert them to utf-8 using python 3
line = line.decode('unicode_escape').encode('latin-1').decode('utf8')
