# Issue on Matching the string and replacing the hex in python
&gt;&gt;&gt; re.sub(r'\\[a-zA-z0-9]{2}', lambda L: str(int(L.group()[2:], 16)), text)
'28-06-20101238212210008:48 PM'
