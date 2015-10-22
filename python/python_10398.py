# How to read special characters of a XML file with minidom
NameValue = unicode(Item.getElementsByTagName("Name")[0].childNodes[0].data.encode("latin-1"), "utf-8")
