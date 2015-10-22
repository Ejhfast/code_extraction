# Find 2 attributes in BeautifulSoup
for entry in soup2:
    if entry.findAll(text=re.compile("Today")):
        print entry
