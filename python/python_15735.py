# Strip unicode character modifiers
import unicodedata
a = u"STRING GOES HERE" # using an actual string would break stackoverflow's code formatting.
u"".join( x for x in a if not unicodedata.category(x).startswith("M") )
