# Extracting XML nodes in Python
from lxml import etree
root = etree.fromstring(your_text)
print root.xpath("//td[contains(text(), 'Image')]/following-sibling::td/a/@href")[0]
