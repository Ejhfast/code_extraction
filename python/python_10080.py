# Getting the XML without the <?xml ...?> from minidom
xml_out = doc.toxml()
return xml_out[22:]
