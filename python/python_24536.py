# using path and beautiful soup on html file converted from pdf
soup = BeautifulSoup(open("output.html"))
doc = open("output.html", "r").read()
tree = etree.HTML(doc)
