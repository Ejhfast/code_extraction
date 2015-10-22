# how to make a single list out of this lists of lists , using list comprehension?
&gt;&gt;&gt; b=[['1','2','3','4','5'],['11','12','13','14','15'],['6','7','8','9','10']]
&gt;&gt;&gt; sorted(int(j) for i in b for j in i)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
