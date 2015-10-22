# Using list to do mathematics in python
l = [('l', '1'), ('l1', '2'), ('l', '1'), ('l', '4')]
print sum(int(x[1]) for x in l)/2. # -&gt; 4.0
