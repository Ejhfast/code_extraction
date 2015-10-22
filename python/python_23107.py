# max-Function for attributes of objects
max_value = max(foo.value for foo in foos)
# instead of:
# max_value = max([foo.value for foo in foos])
