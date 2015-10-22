# UPDATE:Sorting a list from a for output from highest to lowest in python
for x in sorted(frequency, key=lambda y: frequency[y]/float(n), reverse=True):
    print x,frequency[x],frequency[x]/float(n)
