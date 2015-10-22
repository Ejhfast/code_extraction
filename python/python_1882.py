# only parse a specific subtree of an XML file
context = etree.iterparse(xmlfile, tag="yourSubTree")
action, elem = context.next()
etree.iterwalk(elem, ...)...
