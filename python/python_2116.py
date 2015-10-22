# Is it possible for BeautifulSoup to work in a case-insensitive manner?
soup.findAll('meta', attrs={'name':re.compile("^description$", re.I)})
