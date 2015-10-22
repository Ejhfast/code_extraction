# python print only the names from text file
with open("malenames.txt") as f:
   for line in f:
      print (line.split()[0])
