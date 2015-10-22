# How to prevent the command line argument from being encoded?
import unicodedata
print len(unicodedata.normalize("NFD", u"\u00C7"))
print len(unicodedata.normalize("NFC", u"\u00C7"))
