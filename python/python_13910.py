# Use Python re to get rid of links
re.sub('&lt;a[^&gt;]+&gt;(.*?)&lt;/a&gt;', '\\1', text)
