# In Python how do you split a list into evenly sized chunks starting with the last element from the previous chunk?
splitlists = [mylist[i:i+n] for i in range(0, len(mylist), n-1)]
splitlists[-1].append(splitlists[0][0])
