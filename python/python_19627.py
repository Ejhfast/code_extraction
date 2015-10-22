# How to convert listof list into single list without import
&gt;&gt;&gt; a = [[1,2], [23,51,6], ["Hi", "hello"]]
&gt;&gt;&gt; [x for xs in a for x in xs]
[1, 2, 23, 51, 6, 'Hi', 'hello']
