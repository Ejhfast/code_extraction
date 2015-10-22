# How to remove an element from a set?
test, empty = [{'', 'a'}, {'b', ''}], {''}
print [x - empty for x in test]
# [set(['a']), set(['b'])]
