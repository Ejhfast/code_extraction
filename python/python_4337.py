# How to derive the week start for a given (iso) weeknumber / year in python
&gt;&gt;&gt; datetime.datetime.strptime('2011, 4, 0', '%Y, %U, %w')
datetime.datetime(2011, 1, 23, 0, 0)
