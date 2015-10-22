# Adding infos to edges/vertices by name
n2id = dict(zip(graph.vs["name"],[v.index for v in graph.vs]))
name = "J. Smith" # name of the vertices you are interested in
neighbors = graph.neighborhood(n2id[name], order=1)
