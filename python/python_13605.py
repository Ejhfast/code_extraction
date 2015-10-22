# How do I find the string between two special characters?
&gt;&gt;&gt; s = "[virus 1 [isolated from china]]"
&gt;&gt;&gt; s.partition('[')[-1].rpartition(']')[0]
'virus 1 [isolated from china]'
