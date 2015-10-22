# Python: get all content of specific XML tags
xml_tag = dom.getElementsByTagName('person')[0]
xml_data = [elem.nodeValue for elem in dom.getElementsByTagName('name')]
