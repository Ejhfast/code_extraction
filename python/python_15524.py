# Get document DOCTYPE with BeautifulSoup
def doctype(soup):
    items = [item for item in soup.contents if isinstance(item, bs4.Doctype)]
    return items[0] if items else None
