# Highest number in list and append
for i in range( len( sort ) ):
    sort[i].append(max(sort[i][1], sort[i][2]))
    print(sort[i][-1])
