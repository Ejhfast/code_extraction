# Python Regular Expression for Extrating URL
In [230]: s = 'Website is: http://www.somesite.com '
In [231]: re.findall('Website is:\s+(\S+)', s)
Out[231]: ['http://www.somesite.com']
