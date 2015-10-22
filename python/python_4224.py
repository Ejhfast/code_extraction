# In lxml, how do I remove a tag but retain all contents?
&gt;&gt;&gt; etree.strip_tags(fragment,'a','c')
&gt;&gt;&gt; etree.tostring(fragment)
'&lt;fragment&gt;text1 inner1 text2 &lt;b&gt;inner2&lt;/b&gt; text3&lt;/fragment&gt;'
