# List comprehension with if-condition
values = ", ".join(["NULL" if x == "" else "\"%s\"" % x for x in row])
