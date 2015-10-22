# Parsing Alexa XML with python
namespaces = {"aws": "http://awis.amazonaws.com/doc/2005-07-11"}
texts = doc.xpath("//aws:TrafficData/aws:DataUrl/text()", namespaces=namespaces)
print texts[0]
