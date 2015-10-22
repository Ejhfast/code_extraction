# Writing specific lines of a text file
lines = [("LC" if i &lt; 3 else "LB")+line for i,line in enumerate(lines)]
