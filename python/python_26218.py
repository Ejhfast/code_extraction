# Draw graph with fixed-positioned edges
xy = attributes.values()
 G.add_node(attributes.pop('id'), dict([('pos', (float(xy[0]),float(xy[1])) )]))
