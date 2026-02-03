class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)


def preorder(root):
    res = []
    if root:
        res += [root.val]
        res += preorder(root.left)
        res += preorder(root.right)
    return res

def inorder(root):
    res= []
    if root:
        res += inorder(root.left)
        res += [root.val]
        res += inorder(root.right)
    return res

def postorder(root):
    res= []
    if root:
        res += postorder(root.left)
        res += postorder(root.right)
        res += [root.val]
    return res

print("Preorder traversal: " , preorder(root))
print("Inorder traversal: " , inorder(root))
print("postorder traversal: " , postorder(root))