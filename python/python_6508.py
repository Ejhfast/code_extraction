# Converting u"string" to "string" in Python without changing encoding
u'\x96'.encode('raw_unicode_escape').decode("cp1252")
