# Any clever way to unescape data from JSON string?
import json
print ''.join(json.loads(yourstring)['error']['data'])
