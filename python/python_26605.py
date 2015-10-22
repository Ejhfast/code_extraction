# Python: forward fill the data in a list
x = [xi if xi or i==0 else x[i-1]
     for i, xi in enumerate(x)]
