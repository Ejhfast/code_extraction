# Getting rid of the encoding in lxml
'&lt;?xml version="1.0"?&gt;\n' + etree.tostring(root, pretty_print = True, encoding = 'ASCII')
