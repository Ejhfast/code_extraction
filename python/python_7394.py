# Reading tuples stored in textfile
for line in codecs.open("data.txt", "r", encoding="utf-8"):
    tup = ast.literal_eval(line)
    print tup[1]
