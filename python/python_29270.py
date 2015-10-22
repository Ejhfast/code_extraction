# Python parsing XML
for item in root.findall('.//{http://www.w3.org/2005/Atom}title'):
    title = item.text
