# Python extract sentence containing word
In [3]: re.findall(r"([^.]*?apple[^.]*\.)",txt)
Out[4]: ['I like to eat apple.', " Let's go buy some apples."]
