# python time conversion into proper time format
&gt;&gt;&gt; datetime(*strptime(s, "%Y-%m-%dT%H:%M:%S+0000")[0:6]).strftime("%B %d, %Y %I:%M %p")
'July 16, 2013 04:14 PM'
