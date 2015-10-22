# is Python list comprehension with access to the index/enumerate possible?
list2 = [x for ind, x in enumerate(list1) if 4 &gt; ind &gt; 0]
