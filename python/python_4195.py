# Python dictionary: Remove all the keys that begins with s
for k in dic.keys():
  if k.startswith('s_'):
    dic.pop(k)
