# How to get XML tag value in Python
soup = BeautifulSoup('your_XML_string')
print soup.find('text').string
