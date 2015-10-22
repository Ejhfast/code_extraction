# More pythonic way to pick multiple element types from tagged data
for i in range(1, 4):
    type_dict['type_%d' % i] = myTree.cssselect('element_type_%d' % i)
