# PYTHON 2.6 XML.ETREE to output single quote for attributes instead of double quote
print etree.tostring(n).replace('"', "'")
