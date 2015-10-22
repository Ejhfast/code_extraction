# How to get particular tag from an xml document in python
for i in tree.findall('.//country'):
    print ET.tostring(i)
