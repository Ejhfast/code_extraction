# Iterate over a potentially empty argument list
for row in zip(*args) if args else [()]:
