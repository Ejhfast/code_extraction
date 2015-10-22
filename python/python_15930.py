# Joining 2 lists to get (a,d,b,e,c,f) instead of (a,b,c,d,e,f)
&gt;&gt;&gt; sum(zip(list1, list2), ())
('a', 'd', 'b', 'e', 'c', 'f')
