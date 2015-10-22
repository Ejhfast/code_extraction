# How to generate unique equal hash for equal dictionaries?
from pprint import pformat
hash(pformat(a)) == hash(pformat(b))
