# Get all nodes of particular name in lxml?
tree = etree.parse(open('./test.xml'))
reviews = tree.findall(".//Review")
