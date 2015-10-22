# How to remove all the white space from string in Python
s = 'This is the                                     Sample text I need to get       all this               but only with single spaces'
' '.join(s.split())
#'This is the Sample text I need to get all this but only with single spaces'
