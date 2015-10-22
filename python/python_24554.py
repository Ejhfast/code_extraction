# How to make an input be only numbers and not allow a more than a certain amount of characters?
s = input("My input ") # for 2.x it will be raw_input
s = int(s) if len(s) &lt;= 3 else int(s[0:3])
