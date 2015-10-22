# Remove class attribute from HTML using Python and lxml
for tag in node.xpath('//*[@class]'):
    tag.attrib.pop('class')
