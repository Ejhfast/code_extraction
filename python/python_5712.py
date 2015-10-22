# UnicodeDecodeError: 'utf8' codec can't decode bytes in position 3-6: invalid data
json.loads(unicode(opener.open(...), "ISO-8859-1"))
