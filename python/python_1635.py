# Serializing list to JSON
import json
list = [1, 2, (3, 4)] # Note that the 3rd element is a tuple (3, 4)
json.dumps(list) # '[1, 2, [3, 4]]'
