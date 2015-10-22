# How do I right-align numeric data in Python?
width = 10
str_number = str(ord('a'))
print 'a%s' % (str_number.rjust(width))
