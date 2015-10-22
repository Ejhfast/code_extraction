# How to count the number of values associated with a key
&gt;&gt;&gt; max(((k, len(v)) for k, v in dic.items()), key=lambda x: x[1])
('attacks', 4)
&gt;&gt;&gt;
