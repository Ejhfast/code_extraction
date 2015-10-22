# Rows of string to List set
s = """2, 200, 487
1, 199, 486"""
print [line.split() for line in s.splitlines()]
