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

def height(root, depth):
    if root is None:
        return depth
    depth += 1
    return max(height(root.left, depth), height(root.right, depth))
    

root = Node(9)
new_nodes = [3, 7, 11, 10, 17, 23, 1, 27]

for i in new_nodes:
    insert(root, i)
    
print(height(root, 0))