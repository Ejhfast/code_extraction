# how to get a list of lists containing the letters of every line from a text
python 3.2
     a=["hello stack overflow community \n", "i like this site \n", "thank you \n"]
     [[list(v) for v in i.split()] for i in a]
