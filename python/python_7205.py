# How to find the nearest nighboring point coordinates in 2d grid using python
tree = KDTree.construct_from_data(geoid)
for line in results:
  nearest = tree.query(query_point=line, t=2)
