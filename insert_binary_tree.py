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

def view(root):
    if root is None:
        return 
    print(root.val)
    view(root.left)
    view(root.right)

root = Node(10)
new_nodes = [3, 7, 11, 17, 23, 1, 10]

for i in new_nodes:
    insert(root, i)
    
view(root)