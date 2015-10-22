# Get rid of leading zeros for date strings in Python?
&gt;&gt;&gt; t=time.strftime('%m/%d/%Y',time.strptime('12/1/2009', '%m/%d/%Y'))
&gt;&gt;&gt; '/'.join( map( str, map(int,t.split("/")) ) )
'12/1/2009'
