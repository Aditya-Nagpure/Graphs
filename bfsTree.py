from collections import deque

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

def bfs(root):
    if not root:
        return []
    
    queue = deque()
    queue.append(root)

    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res

print("BFS Traversal: ", bfs(root))

