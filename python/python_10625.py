# Loop construct in Python
print [z for z in range(10000) if all(z%k==0 for k in range(1,10))]
&gt;&gt;&gt; [0, 2520, 5040, 7560]
