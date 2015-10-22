# Python binary tree serializing problem
def convert_to_jtree(bt):
    return JTree(bt.data, [convert_to_jtree(bt.left) if bt.left else None,
                          convert_to_jtree(bt.right) if bt.right else None])
