# how to: convert dictionary to strings in Python?
for key in data:
  exec("{0} = '{1}'".format(key,data[key]))
