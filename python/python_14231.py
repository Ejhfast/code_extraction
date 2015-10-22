# How to best iterate (breadth-first) over an lxml etree using Python
for child in doc.getroot().iterchildren("*"):
    print(child.tag, child.attrib)
