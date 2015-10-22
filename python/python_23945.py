# UnicodeEncodeError: 'ascii' codec can't encode character u'\u2013'
print(u'\n'.join('{}:{}'.format(w.encode('utf-8'), f).decode('utf-8') for f,w in words))
