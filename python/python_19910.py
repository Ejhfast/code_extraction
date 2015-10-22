# What is the good python3 equivalent for auto tuple unpacking in lambda?
min(points, key=lambda p: (lambda x,y: (x*x + y*y))(*p))
