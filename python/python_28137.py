# Pair string lengths to strings from unordered list
&gt;&gt;&gt; { str(len(x)) : x for x in py_list if not x.isdigit() and str(len(x)) in py_list }
{'1': '#', '3': '###', '2': '##', '4': '####'}
