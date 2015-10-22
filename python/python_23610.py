# Functional solution for looping through nested dictionaries
d={"A":{"B":{"C":"FOO"}}}
[(k1,k2,k3,v3) for k1,v1 in  d.items() for k2,v2 in v.items() for k3,v3 in v1.items()]
