# Select all anchor tags with an href attribute that contains one of multiple values via xpath in lxml / Python
sites=['aaa', 'bbb']
contains = ' or '.join('contains(@href,(%s))' % site for site in sites)
anchor_xpath = etree.XPath('//a[%s][descendant::img]' % contains)
