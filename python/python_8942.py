# Unicode encoding for filesystem in Mac OS X not correct in Python?
filename = unicodedata.normalize('NFC', unicode(filename, 'utf-8')).encode('utf-8')
