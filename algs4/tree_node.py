class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def traverse(self):
        print(self.val)
        self.traverse(self.left)
        self.traverse(self.right)
