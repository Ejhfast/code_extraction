# How to check for adjacency in list, then fix adjacency in python
row = ["0","0","0","0","0","0","0","0","0","01","01","01","01","01","01"]
random.shuffle(row)
print (map(int, list("".join(row)[1:])))
