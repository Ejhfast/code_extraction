# Python urlencode don't encode special characters
mydict = {'key1': 'value@1', 'key2': 'value@2'}
&gt;&gt;&gt; "&amp;".join("{}={}".format(*i) for i in mydict.items())
'key2=value@2&amp;key1=value@1'
