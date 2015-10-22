# Sorting xml nodes by attributes using xml.dom.minidom
nodes = dom.getElementsByTagName('Node')
nodes.sort(key=lambda x: int(x.attributes['Position'].value))
