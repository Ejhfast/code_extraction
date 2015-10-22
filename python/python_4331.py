# python filter string only showing tags less than 2 words
[item.strip() for item in mystring.split(',') if len(item.split()) &lt; 2]
