# Python Lxml (objectify): Checking whether a tag exists
tree = etree.parse(StringIO(htmlString), etree.HTMLParser()).getroot()
youWantValue = tree.xpath('/main/elem2')[0].text
