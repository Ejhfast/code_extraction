# Convert a string of numbers into numbers and leaving the date a string in python
&gt;&gt;&gt; s = ['4/5/2013', '19.7', '20.35', '19.69', '20.3', '521000', '19.02']
&gt;&gt;&gt; [float(i) if not '/' in i else i for i in s]
['4/5/2013', 19.7, 20.35, 19.69, 20.3, 521000.0, 19.02]
