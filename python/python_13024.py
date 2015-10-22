# Iterating and printing JSON objects in Python
for entry in j['feed']['entry']:
    print entry['title']['$t']
