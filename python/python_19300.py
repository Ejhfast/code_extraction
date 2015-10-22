# Write to a file to bypass memory cap when generating a big variable. Python 3.3
for i in itertools.product(string.ascii_letters + string.digits, repeat=8):
     print(''.join(i))
