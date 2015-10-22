# lxml not adding newlines when inserting a new element into existing xml
parser = etree.XMLParser(remove_blank_text=True)
pom = etree.parse("pom.xml",parser)
