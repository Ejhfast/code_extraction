# Remove strings from a list that contains numbers in python
[x for x in my_list if not any(c.isdigit() for c in x)]
