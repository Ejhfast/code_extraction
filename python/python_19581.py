# Unable to scrap data with beautiful soup in python
elem = soup.find('input',{'id':'short-link-input'})
print elem.get('value')
