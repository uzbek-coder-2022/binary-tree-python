class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None
        
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return None
    if root.val > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        
    return root
        
def preorder_traversal(root, lst):
    if root is not None:
        lst.append(root.val)
        preorder_traversal(root.left, lst)
        preorder_traversal(root.right, lst)
        
def inorder_traversal(root, lst):
    if root is not None:
        inorder_traversal(root.left, lst)
        lst.append(root.val)
        inorder_traversal(root.right, lst)
        
def postorder_traversal(root, lst):
    if root is not None:
        postorder_traversal(root.left, lst)
        postorder_traversal(root.right, lst)
        lst.append(root.val)

root = Node(13)
new_nodes = [7, 2, 9, 19]

for i in new_nodes:
    insert(root, i)

node_values = []
postorder_traversal(root, node_values)


print(node_values)