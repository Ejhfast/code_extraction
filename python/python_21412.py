# Pattern matching and replacing in Python
import re
print re.sub(r'\[URL\](.*?)\[/URL\]',r'&lt;a href="\1"&gt;\1&lt;/a&gt;', "Hello here is a [URL]www.url.com[/URL] and it's great.")
