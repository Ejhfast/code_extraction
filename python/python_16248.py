# Turning a two dimensional list into a dictionary in python
result = {}
for item in data:
    result.setdefault(item[0], {}).update({item[1]: item[2]})
