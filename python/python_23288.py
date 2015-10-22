# Reading an XML file as is (with indentation) in a variable (using Python)
import lxml.etree as etree
x = etree.parse("filename")
print etree.tostring(x, pretty_print = True)
