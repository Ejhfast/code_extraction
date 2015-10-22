# Python style: more concise way to rename a variable while checking it is not null
for name in (data['name'],) if data['name'] else ():
    print name
