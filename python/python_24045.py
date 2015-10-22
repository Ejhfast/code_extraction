# Parsing XML data with nested tags in Python
d = collections.defaultdict(list)
for element in rootElement.iter():
    d[element.tag].append(element.text)
