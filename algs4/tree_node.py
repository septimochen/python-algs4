class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(t):
    if t is None:
        return
    else:
        traverse(t.left)
        traverse(t.right)
        print(t.val)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    # traverse(tree)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(7)
    tree.right.right = TreeNode(5)
    tree.right.left = TreeNode(8)
    traverse(tree)
