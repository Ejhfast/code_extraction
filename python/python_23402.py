# Python adding lists of numbers with other lists of numbers
&gt;&gt;&gt; lists = (listOne, listTwo, listThree)
&gt;&gt;&gt; [sum(values) for values in zip(*lists)]
[10, 9, 16, 11, 13]
