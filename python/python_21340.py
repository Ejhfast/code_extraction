# Read weighted graph using "igraph" in python
g = igraph.Nexus.get("karate")
for edge in g.es:
    print edge["weight"]
