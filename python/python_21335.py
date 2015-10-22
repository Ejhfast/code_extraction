# Create a weighted graph from an adjacency matrix in graph-tool, python interface
adj = numpy.random.randint(0, 2, (100, 100)) # a random directed graph
g = Graph()
g.add_edge_list(transpose(adj.nonzero()))
