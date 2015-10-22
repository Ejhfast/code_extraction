# Python String to Date?
&gt;&gt;&gt; from datetime import datetime
&gt;&gt;&gt; datetime.strptime('130129:1007', '%y%m%d:%H%M')
datetime.datetime(2013, 1, 29, 10, 7)
