# Parse JSON in Python
import json
j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
print j['two']
