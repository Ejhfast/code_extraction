# List of numbers whose squares are the sum of two squares
x = [(a,b,c) for c in range(1,1001) for b in range(1, c) for a in range(1,b) if a**2+b**2==c**2]
print x
