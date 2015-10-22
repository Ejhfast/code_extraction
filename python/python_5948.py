# Can I do math inside Python's string formatting "language"?
N = { 'd' : 3 }
four = Template(u'number:{{ d + 1 }}').render(**N)
