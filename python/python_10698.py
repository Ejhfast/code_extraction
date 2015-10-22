# Nested list comprehension equivalent
&gt;&gt;&gt; l = ['1\t2,3\t4,5', '61\t7,8\t9,0']
&gt;&gt;&gt; [[i[0]]+[e.split(',') for e in i[1:]] for i in [x.split() for x in l]]
[['1', ['2', '3'], ['4', '5']], ['61', ['7', '8'], ['9', '0']]]
