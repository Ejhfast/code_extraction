# Recursive sequence $x_n = \sqrt{2}$, $x_{n+1} = \sqrt{2x_n}$
X = [sqrt(2)]
for i in range(1,10):
    X.append(sqrt(2*X[i-1]))
