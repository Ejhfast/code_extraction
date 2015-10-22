# python convert date and time into linux timestmap
&gt;&gt;&gt; s =  "110202 132721"
&gt;&gt;&gt; print time.mktime(time.strptime(s, "%y%m%d %H%M%S"))
1296653241.0
