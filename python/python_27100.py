# Python Regex/Beautiful Soup Wild Card
finder = re.compile('div_(\w\w\w)_basic')
print re.findall(finder, str(soup))
for soup_ in soup.find_all("div", {"id" : finder}):
