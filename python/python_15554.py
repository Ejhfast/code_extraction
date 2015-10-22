# Efficient extraction of a subgraph according to some edge attribute in NetworkX
&gt;&gt;&gt; G = nx.DiGraph(((source, target, attr) for source, target, attr in my_network.edges_iter(data=True) if attr['weight'] &gt; threshold))
