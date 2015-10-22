# C# / Python Encoding difference
import codecs
with codecs.open(filename, encoding="utf-8") as inp:
    text = inp.read()
