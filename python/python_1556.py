# Using SimpleXMLTreeBuilder in elementtree
from xml.etree import ElementTree # part of python distribution
from elementtree import SimpleXMLTreeBuilder # part of your codebase
ElementTree.XMLTreeBuilder = SimpleXMLTreeBuilder.TreeBuilder
