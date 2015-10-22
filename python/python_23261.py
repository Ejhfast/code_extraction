# Searching attributes of an XML's element tree with xml.etree.ElementTree
# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")
