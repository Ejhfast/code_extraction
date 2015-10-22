# On Windows, how to convert a timestamps BEFORE 1970 into something manageable?
&gt;&gt;&gt; datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=-2082816000)
datetime.datetime(1904, 1, 1, 8, 0)
