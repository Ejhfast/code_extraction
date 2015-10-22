# How to find if the data is a str or int in List
for i in xrange(len(samplist)):
    if isinstace(samplist[i], str):
        samplist[i] += 'def'
