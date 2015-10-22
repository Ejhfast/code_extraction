# What is the best way to calculate percentage of an iterating operation?
percent_quota=0  #starting value
for i in range(limit_min,limit_max+1):  #we make sure all lengths are covered
    percent_quota+=(10**i)-1  #we subtract 1 because for length of 2, max is 99
