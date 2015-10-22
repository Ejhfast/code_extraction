# using BeautifulSoup to insert an element before closing body
soup.body.insert(len(soup.body.contents), yourelement)
