# Django MPTT : Filter by depth?
# Retrieve root nodes and their immediate children only
SomeModel.tree.filter(level__lte=1)
