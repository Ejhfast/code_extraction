# Handling exception with BeautifulSoup
price = individual_page.find("span", {"class","black20b"})
if price:
    print ''.join(price.findAll(text=True))
