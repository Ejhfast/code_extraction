# How to make XPath return 'None' in Python if no data found?
In [16]: [x.text for x in bk.xpath("//book/*")]
Out[16]: ['Harry Potter', '29.99', None, 'Learning XML', '39.95', None]
