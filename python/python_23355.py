# Python - nested comprehension list
output=[{input[el]['feature']:input[el]['value']
  for el in input[name]['elements']} for name in lnames]
