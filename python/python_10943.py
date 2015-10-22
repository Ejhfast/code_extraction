# HTML parse with python and bs
for a in soup.findAll("a", "title"):
    print a.get_text()
