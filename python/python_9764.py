# Error with lxml syntax to parse table elements while validating column contents
&gt;&gt;&gt; doc.xpath('//tr/td[contains(text(),"Street :")]/span/text()')
[' High St. ']
