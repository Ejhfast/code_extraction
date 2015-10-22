# Pythonic way to iterate through loops
for row in table.findAll('tr', attrs = {'class':'odd'}) + table.findAll('tr', attrs = {'class':'even'}):
    for cell in row.findAll('td'):
        print cell
