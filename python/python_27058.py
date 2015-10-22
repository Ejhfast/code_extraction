# How to use a 'for' loop to iterate nested-list index items in Python 2.7?
for i in range(1,len(nList)):
    for distance in nList[i]:
        outputLlist.append('{} metres, {} metres, {} seconds'.format(*distance))
