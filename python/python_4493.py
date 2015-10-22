# Find all links inside a table
html = BeautifulSoup(page)
table = html.find('table', 't1')
links = table.findAll('a')
