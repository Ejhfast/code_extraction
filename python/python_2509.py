# Get table with maximum number of rows in a page using BeautifulSoup
number_of_rows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))
