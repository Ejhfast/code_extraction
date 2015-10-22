# Avoid using two arrays to make a simple string change
jsonlist = ['foo.json', 'bar.json']
print [item.replace(".json", "") for item in jsonlist]
# ['foo', 'bar']
