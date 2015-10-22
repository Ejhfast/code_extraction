# how to prevent xpath adding commas on encountered tags
In [3]: import re
In [4]: [re.sub('&lt;[^&lt;]+?&gt;', '', x) for x in response.xpath('/a').extract()]
Out[4]: [u'C-(K1, K2)-convexity']
