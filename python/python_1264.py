# app engine: string to datetime?
&gt;&gt;&gt; import datetime
&gt;&gt;&gt; datetime.datetime.strptime(date + ' ' + hour + ':' + minutes + ':' + seconds, '%m/%d/%Y %H:%M:%S')
datetime.datetime(2009, 11, 28, 23, 59)
