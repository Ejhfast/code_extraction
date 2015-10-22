# how to translate matlab function max(y(x>3)>2) to numpy in single line
max([y[i] for i in range(len(y)) if x[i] &gt; 3 and y[i]&gt;2])
