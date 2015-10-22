# Remove <br> tags from a parsed Beautiful Soup list?
for e in soup.findAll('br'):
    e.extract()
