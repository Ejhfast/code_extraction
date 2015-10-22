# Adding a separate element using list comprehensions
root = TreeNode("Level " + str(i), Array[TreeNode](
    [TreeNode(x) for x in l[i]] + [root]))
