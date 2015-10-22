# Is parsing XML really this ugly in python?
import xml.etree.ElementTree as ET
tree = ET.parse(filePath)
data = float(tree.find('InfoType/SpecificInfo')[0].text)
