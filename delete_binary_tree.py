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

def delete(root, key):
    if root is None:
        return root
    
    if root.val < key:
        root.right = delete(root.right, key)
    elif root.val > key:
        root.left = delete(root.left, key)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        temp = get_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
        
    return root
        
def get_min(root):
    while root.left is not None:
        root = root.left
        
    return root

def visual(root, depth):
    if root is not None:
        visual(root.right, depth+1)
        print(3*depth * ' ', root.val)
        visual(root.left, depth+1)
        
root = Node(15)
new_nodes = [7, 1, 24, 19, 16, 27, 30]

for i in new_nodes:
    insert(root, i)
    
visual(root, 0)

delete(root, 27)

visual(root, 0)