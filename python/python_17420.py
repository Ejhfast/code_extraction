# Generating a list of all strings possible using 6 characters
list("".join(l) for l in itertools.product('ABCDEF', repeat=4))
