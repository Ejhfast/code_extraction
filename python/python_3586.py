# Please help extract text from HTML tags using Python Regex
re.match(r'.*&gt;([^&lt;&gt;]*)&lt;/font&gt;.*', s).group(1)
