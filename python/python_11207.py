# Files gets closed after evaluation of a generator expression
with open('test.txt') as f:
    for i in f:
        print("&gt;", i, end="")
