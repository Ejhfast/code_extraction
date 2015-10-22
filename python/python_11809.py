# Correct syntax for nested list or set comprehension
tags = set(tag  for e in my_obj['Episodes'] for tag in e['Tags'])
