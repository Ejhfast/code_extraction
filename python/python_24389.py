# extracting data between span tags with BeautifulSoup Python
Matching an optional '#' does not seem to be working properly
s = 'spamword'
re.findall(r'#?' + s + r'\b', text)
