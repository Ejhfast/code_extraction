# When adding to list why does Python copy values instead of pointers?
a,b,c  =  [ 1 if i&gt;1 else i for i in [ a, b, c ] ]
a,b,c = map( lambda x: 1 if x&gt;1 else x, [a,b,c] ) #lambda or name of some function
