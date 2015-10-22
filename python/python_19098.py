# saving stdout into a variable in a doctest
output = Popen(["mycmd", "myarg"], stdout=PIPE).communicate()[0]
