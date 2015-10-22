# Python: Get data between html tags if an attribute matches and put it into a list
pattern = '&lt;td.*?bgcolor="#ff9900".*?>(.*?)&lt;/th>'
re.findall(pattern, html)
