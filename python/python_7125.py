# Faster alternative to BeautifulSoup for parsing visible text in an html file
find . -name '*.html' -exec w3m -dump {} \;
