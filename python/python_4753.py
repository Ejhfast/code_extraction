# replace empty string(s) in tuple
tuple('-' if x == '' else x for x in tup)
