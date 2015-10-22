# How to iterate through all nodes of a tree?
for subtree in tree.subtrees():
    s = subtree.label()
    subtree.set_label(re.sub('-.*', "", s))
