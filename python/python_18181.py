# How to create a tree in NetworkX and display it in D3.js
&gt;&gt;&gt; from networkx.readwrite import json_graph
&gt;&gt;&gt; G = nx.DiGraph([(1,2)])
&gt;&gt;&gt; data = json_graph.tree_data(G,root=1)
