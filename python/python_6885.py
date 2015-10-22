# Reading Elements by attribute Condition lxml
from lxml import etree
xml = etree.parse(open('1.xml'))
xml.xpath("//qtn[@state="+state+"]/text()")
