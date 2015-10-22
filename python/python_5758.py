# fast parsing links out of a page in python
root = lxml.html.fromstring(s)
anchors = root.cssselect("a")
links = [a.get("href") for a in anchors]
