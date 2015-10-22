# urlparse completely failing on every url
x = "&lt;a href='http://www.bbcnews.com'&gt;foo&lt;/a&gt;"
link_exp.findall(x)
# ["'http://www.bbcnews.com"]
