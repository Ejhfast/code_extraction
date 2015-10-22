# Sorting a list depending on every other element in python
ls = ["Milan", 6, 2, "Inter", 3, 2, "Juventus", 5, 2]
&gt;&gt;&gt; sorted([ls[i:i+3] for i in range(0,len(ls),3)], key=lambda x:x[1])
[['Inter', 3, 2], ['Juventus', 5, 2], ['Milan', 6, 2]]
