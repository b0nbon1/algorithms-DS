class TreeNode:
    def __init__(self, value, left= None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def walk(curr, path):
    if not curr:
        return path
    # recurse steps
    # pre
    # recurse
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)
    # post
    return path

def in_order_search(head):
    path = []
    walk(head, path)
    return path

tree = TreeNode(20)
tree.left = TreeNode(10)
tree.right = TreeNode(50)
tree.left.right = TreeNode(15)
tree.left.left = TreeNode(5)
tree.left.left.right = TreeNode(7)
tree.left.left.left = TreeNode(4)
tree.right.left = TreeNode(30)
tree.left.right.left = TreeNode(45)
tree.left.right.right = TreeNode(55)
tree.right.left.right = TreeNode(29)
tree.right.left.left = TreeNode(32)
tree.right.right = TreeNode(100)
tree.right.right.left = TreeNode(107)
tree.right.right.right = TreeNode(103)

print(in_order_search(tree))
