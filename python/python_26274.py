# Python regex on phone numbers
&gt;&gt;&gt; s = 'blah +442032398869 blah +1 (888) 2572054blah'
&gt;&gt;&gt; re.findall(r'\(?\+[\d _\-\.\)\(\+]{8,25}[\d]{1}', s)
['+442032398869', '+1 (888) 2572054']
