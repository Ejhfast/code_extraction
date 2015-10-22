# how to get a nested element?
&gt;&gt;&gt; [a.text.strip() for a in soup.find_all('a', {'itemprop': 'replyToUrl'})]
[u'#41', u'#42', u'#43', u'#44', u'#45', u'#46', u'#47', u'#48', u'#49', u'#50']
