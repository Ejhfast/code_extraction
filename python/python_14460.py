# Python - Remove URLs from text with regex
p=re.compile(r'\&lt;http.+?\&gt;', re.DOTALL)
re.sub(p, '', plain)
