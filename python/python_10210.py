# How do I remove dicts from a list with duplicate fields in python?
dict((x['id'], x) for x in L).values()
