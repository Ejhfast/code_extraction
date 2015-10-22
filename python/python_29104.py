# BeautifulSoup - check if elements have specific class
for node in soup.find_all(attrs={"class": re.compile(r'my_class(1|2)')}):
    print(node)
