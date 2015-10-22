# grab tweet with python encounters UnicodeEncodeError
for item in list:
    print item[u'text'].encode('utf-8')
