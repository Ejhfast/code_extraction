# pythonic way of checking endpoints of a list against two sets of valid entries
if path[0] in endpoint1 and path[-1] in endpoint2 or \
   path[0] in endpoint2 and path[-1] in endpoint1:
