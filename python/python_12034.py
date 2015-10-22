# Python XML- getting what is between two nodes
gui = minidom.parse("path to xml").getElementsByTagName('gui')[0]
gui.getElementsByTagName('object')[0].toxml()
