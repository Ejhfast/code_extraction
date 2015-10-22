# Python: getting filename case as stored in Windows?
&gt;&gt;&gt; import win32api
&gt;&gt;&gt; win32api.GetLongPathName(win32api.GetShortPathName('texas.txt')))
'TEXAS.txt'
