# UnicodeEncodeError: 'ascii' codec can't encode character when trying a HTTP POST in Python
name = u'\xe4\xf6\xfc'.encode('utf-8')
userInfo = [('Name', name)]
