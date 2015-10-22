# get document with fields (and no value) present in other documents
for user in users:
    print("{n} said : {s}".format(n=user['name'], s=user.get('last_say', 'Nothing!')))
