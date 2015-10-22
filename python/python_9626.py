# Regular Expression Match/Replace
&gt;&gt;&gt; x = re.search("sub(\d+)\.domain\.com\/(\d+)","sub123.domain.com/546").groups()
('123', '546')
&gt;&gt;&gt; url = "%s blah blah %s" % x
