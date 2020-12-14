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
        print(t.val)
        traverse(t.right)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    traverse(tree)
