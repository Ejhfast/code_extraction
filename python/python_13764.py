# Get the inner HTML of a element in lxml
from lxml import etree
print(etree.tostring(root, pretty_print=True))
