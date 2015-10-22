# Pascal's Triangle with iterative algorithm via list comprehension in Python
[d.setdefault(j, [sum(d[len(d)-1][max(i, 0):i + 2]) for i in range(-1, j)])
 for j, d in enumerate([{0: [1]}] * 5)]
