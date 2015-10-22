# Python encoding problems
text = unicodedata.normalize('NFD', text).encode('ascii','ignore')
