# How to call variables generated in loop
dict1 = {'imp_local'+str(k):700 for k,val in enumerate(nBottom)}
dict2 = {'imp_global'+str(k):600 for k,val in enumerate(nBottom)}
