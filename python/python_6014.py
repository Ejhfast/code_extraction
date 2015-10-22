# Is there an elegant way to count tag elements in a xml file using lxml in python?
import lxml.etree
doc = lxml.etree.parse(xml)
count = doc.xpath('count(//author)')
