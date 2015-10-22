# Python Time Delta time data does not match format error, can't find my mistake
&gt;&gt;&gt;import datetime
&gt;&gt;&gt;datetime.datetime.strptime('2015-07-30 20:32:01.521834', '%Y-%m-%d %H:%M:%S.%f')
&gt;&gt;&gt;datetime.datetime(2015, 7, 30, 20, 32, 1, 521834)
