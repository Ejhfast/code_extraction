# How to convert string date to a epoch timestamp in python
&gt;&gt;&gt; import time
&gt;&gt;&gt; time.mktime(time.strptime('2015-03-25T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ'))
1427241600.0
