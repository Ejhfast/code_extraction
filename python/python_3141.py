# Python: Strange behaviour of recursive function with keyword arguments
def node_depth(node, depth=0, colored_nodes=None):
    ...
    if colored_nodes is None: colored_nodes = set()
