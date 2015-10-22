# Reading XML with
from xml.etree import ElementTree
tree = ElementTree.fromstring('&lt;icon&gt;&lt;author&gt;Author Name&lt;/author&gt;&lt;/icon&gt;')
print tree.find('author').text
