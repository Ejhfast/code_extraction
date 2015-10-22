# Why the result is incorrect to find 3-cliques using networkx in Python?
import itertools
cliques3 = set(sum([list(itertools.combinations(set(clq), 3)) for clq in cliques if len(clq)&gt;=3],[]))
