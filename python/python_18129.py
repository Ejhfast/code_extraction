# How to improve the following list-to-list look up in Python?
&gt;&gt;&gt; [('-1' if item not in list_B else item) for item in list_A]
['-1', '-1', '2', '-1', '-1', '-1', '6', '7']
