# Replacing string and characters in front of it in Python
with open("new.txt", "wt") as out:
    for line in open("source.txt"):
        out.write('/' + line.rsplit('/', 1)[1])
