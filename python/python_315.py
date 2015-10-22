# PY: Url Encode without variable name
import urllib
q = ['with space1', 'with space2']
qescaped = map(urllib.quote, q)
