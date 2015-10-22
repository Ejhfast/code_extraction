# Grab Content from XML using Python? almost there
for node in Tree.getiterator():
    print node.tag, node.attrib, node.text
