# How to format a string into a two column list
inputText = "x1 y1\n x2 y2\n x3 y3\n"
print [line.split() for line in inputText.split('\n') if line]
