# Unpack List in List Comprehension
&gt;&gt;&gt; [x for a in arg if dictAll.has_key(a) for x in dictAll[a]]
['one', 'two', 'three']
