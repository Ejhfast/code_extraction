# Combine date column and time column into datetime column
&gt;&gt;&gt; df.apply(lambda x: combine(x['MEETING DATE'], x['MEETING TIME']), axis=1)
0   2013-12-16 14:00:00
1   2013-12-12 13:00:00
