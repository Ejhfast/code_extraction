# Parsing XML using json raises ValueError
import json
print json.loads("other_npc_name") #throws error
print json.loads('"other_npc_name"') #returns "other_npc_name" as a Unicode string
