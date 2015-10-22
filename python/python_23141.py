# BeautifulSoup: Parse children by tag name
geo = soup.find('geo')
print geo.lat.get_text(strip=True)
print geo.lng.get_text(strip=True)
