# Python sorting a list of dictionaries with if statement
sortedlist = sorted([x for x in dicts if x['student']==1], key=lambda k:k['age'])
