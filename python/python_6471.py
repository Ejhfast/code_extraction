# When using iterdescendants() on an etree, is it ok to modify the tree?
for element in doc.iterfind('.//%s'%tag):
    element.getparent().remove(element)
