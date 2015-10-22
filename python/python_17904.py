# matching commas in BeautifulSoup
expression = re.compile('\,[\s\w()-]+\,')
textnode = HTML.body.p.find_all(text=expression)
print expression.search(textnode).group(0)
