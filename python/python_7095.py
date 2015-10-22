# how do you split a string to create nested list?
&gt;&gt;&gt; s = '1,55,6,89,2|7,29,44,5,8|767,822,999'
&gt;&gt;&gt; [[int(x) for x in ss.split(',')] for ss in s.split('|')]
[[1, 55, 6, 89, 2], [7, 29, 44, 5, 8], [767, 822, 999]]
