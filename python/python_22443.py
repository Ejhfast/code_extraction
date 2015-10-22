# Unpack only the first few columns from the CSV reader?
with open("foo.csv") as foo:
    for a,b in (r[0:2] for r in csv.reader(foo)):
         ...
