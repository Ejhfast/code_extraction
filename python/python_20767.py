# How to best extract the following content in html string in python?
regex = re.compile(r'&gt;Settlement Date:&lt;/td&gt;[^&gt;]*&gt;([^&lt;]*)')
match = regex.search(data)
print match.group(1)
