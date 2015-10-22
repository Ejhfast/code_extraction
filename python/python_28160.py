# Wrong colors for weighted edges in NetworkX
edges, colors = zip(*nx.get_edge_attributes(G,'weight').items())
nx.draw(G, pos, edgelist=edges, edge_color=colors, width=10, edge_cmap = plt.cm.jet, vmin = 0.0, vmax = max(weights.values()))
