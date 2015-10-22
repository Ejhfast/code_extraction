# Python - How to raise a value error of multiple items in list
if len(l1) != 8 or len([n for n in l1 if n not in (1, 0)]) != 0:
  raise ValueError('Invalid entries or incorrect length')
