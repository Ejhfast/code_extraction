# How to find element attribute using lxml
rating = node.xpath('//t:rating', namespaces = {'t':'http://example/namespace'})
print rating[0].attrib['system']
