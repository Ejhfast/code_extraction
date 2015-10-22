# How do I make BeautifulSoup parse the contents of textarea tags as HTML?
for textarea in soup.findAll('textarea'):
    contents = BeautifulSoup.BeautifulSoup(textarea.contents[0]).renderContents()
    textarea.replaceWith(contents)
