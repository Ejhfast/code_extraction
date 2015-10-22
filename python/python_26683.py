# python sort list of lists based on inner element AND ignore case
&gt;&gt;&gt; sorted([[1, 'C'], [2, 'D'], [3, 'a'], [4, 'b']], key=lambda x: x[1].lower())
[[3, 'a'], [4, 'b'], [1, 'C'], [2, 'D']]
