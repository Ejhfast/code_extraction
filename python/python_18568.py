# Get all tagged text under li tags
import re
re.findall(r'&lt;li&gt;&lt;strong&gt;([^&lt;]*)&lt;/strong&gt;&lt;/li&gt;', my_text)
