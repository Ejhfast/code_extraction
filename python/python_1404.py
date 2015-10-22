# Is there a better way to compare dictionary values
diffkeys = [k for k in dict1 if dict1[k] != dict2[k]]
for k in diffkeys:
  print k, ':', dict1[k], '-&gt;', dict2[k]
