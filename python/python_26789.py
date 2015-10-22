# How can I generate a bracketed tree string in NLTK from a list of nodes and their children
dg = DependencyGraph(conll_data1)
tree = dg.tree()
tree.pprint()
