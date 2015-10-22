# python: iterate through list and replace elements with corresponding dictionary values
D2 = dict((x['id'], x['val']) for x in D)
L2 = [D2[x] for x in L]
