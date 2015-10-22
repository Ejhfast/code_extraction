# python regular expression replace
p = re.compile('&lt;/span&gt;&lt;/p&gt;\r\n&lt;p&gt;&lt;span class=font\d&gt;(?=[a-z])')
res = p.sub(' ', data)
