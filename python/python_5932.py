# How to read and parse XML without schema in Python?
import xml.etree.ElementTree
tree = xml.etree.ElementTree.parse("foo.xml")
myArray = [int(x.text) for x in tree.getroot().findall("human/weight")]
