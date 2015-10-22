# Python implementation of set relations
S = [1,2,3,4,5,6]
result = [ (x,y) for x in S for y in S if y%x==0]
