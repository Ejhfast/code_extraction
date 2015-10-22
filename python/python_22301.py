# Use variable in variable name
for i in range(1, 256):
    name = "key{}".format(i)
    print globals()[name]
