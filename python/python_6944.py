# Python decode text to ascii
In [1]: import urllib
In [2]: urllib.unquote(urllib.unquote("what%2527s%2bthe%2btime%252c%2bnow%253f") )
Out[3]: "what's+the+time,+now?"
