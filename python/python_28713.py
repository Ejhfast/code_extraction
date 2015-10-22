# Accessing child XML elements with XPATH in Python
for a in parsed.xpath("//c:Reaction", namespaces=NSMAP):
    for b in a.xpath(".//c:Constant", namespaces=NSMAP):
        print b.attrib['name']
