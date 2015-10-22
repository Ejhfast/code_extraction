# Weighted Degree Distribution in Python's graph_tool
d = g.degree_property_map("out", weight)   # weight is an edge property map
bins = linspace(d.a.min(), d.a.max(), 40)  # linear bins
h = vertex_hist(g, d, bins)
