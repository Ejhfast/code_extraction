# Scraping value from field on a page
for a in soup.findAll('a'):
    if a.has_attr('data'):
        print(a['data'])
