# how to extract a particular node in xml using xpath in python
&gt;&gt;&gt; result.xpath('//*[local-name()="IFrameURL"]/text()')[0].strip()
'http://www.amazon.com/reviews/iframe?akid=[AWS Access Key ID]&amp;asin=0316067938&amp;exp=2011-08-01T17%3A54%3A07Z&amp;linkCode=xm2&amp;summary=0&amp;tag=ws&amp;truncate=256&amp;v=2&amp;sig=[Signature]'
