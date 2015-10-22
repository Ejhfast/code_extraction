# Sentence processing in Python
with open('topon.txt') as infile:
  for line in infile:
    print line.split('.', 1)[0]
