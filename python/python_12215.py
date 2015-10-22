# Get the common prefix substring through Regex
match = re.search(r'(?m)\A(.*).*(?:\n?^\1.*$)*\n?\Z', text)
