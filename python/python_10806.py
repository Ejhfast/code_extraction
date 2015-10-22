# Processing Utf-8 data in python
ascii_string = unicodedata.normalize('NFKD', unicode_string).encode('ascii','ignore')
