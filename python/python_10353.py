# python: select a list of instances by checking the items in a member variable (list) of each instance
newl = [ n for n in l if all([ m % 3 == 0  for m in n.memList]) ]
