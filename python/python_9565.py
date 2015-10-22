# processing of list of list
&gt;&gt;&gt; x = [['a','a','a'],['b','b','b'],['c','c','c'],['d','d','d']]
&gt;&gt;&gt; map('_'.join, zip(*x))
['a_b_c_d', 'a_b_c_d', 'a_b_c_d']
