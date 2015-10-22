# how to edit and update xml files in a directory in python
with open("outfile.xml", "w") as f:
    f.write(etree.tostring(xmlData))
