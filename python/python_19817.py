# reading a set of points from file and making a .OFF file
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write("[" + ", ".join(line.strip().split()) + "]\n")
