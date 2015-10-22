# How to ignore the time while converting string to date?
d = datetime.datetime.strptime("2011-10-13", "%Y-%m-%d")
print d.date()
&gt;&gt; 2011-10-13
