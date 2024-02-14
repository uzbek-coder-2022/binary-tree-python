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

def visual(root, depth):
    if root is not None:
        visual(root.right, depth+1)
        print(3*depth * ' ', root.val)
        visual(root.left, depth+1)
        

root = Node(13)
new_nodes = [10, 7, 12, 15, 19, 17, 18, 22]

for i in new_nodes:
    insert(root, i)
    
visual(root, 0)