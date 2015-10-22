# How to recursively traverse an XML File in Python?
for child in [child for child_root in tree_root for child in child_root]:
    print(child)
