# Accessing multiple dictionary values
&gt;&gt;&gt; {i: {j: (d[i][j], e[j]) for j in d[i]} for i in d}
{u'1': {1746L: (1, 3), 2239L: (1, 2)}, u'3': {2056L: (4, 3), 2425L: (1, 4)}, u'2': {1965L: (2, 3)}}
