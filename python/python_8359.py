# Adding newlines in a list of lists
el = [0, ['~', '~', '~'], 1, ['~', '~', '~'], 2, ['~', '~', '~'] ]
for i in range(0, len(el), 2):
    print el[i], " ".join(el[i+1])
