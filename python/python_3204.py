# Replace non-ascii chars from a unicode string in Python
&gt;&gt;&gt; import unicodedata
&gt;&gt;&gt; unicodedata.normalize('NFKD', u"m\u00fasica").encode('ascii', 'ignore')
'musica'
