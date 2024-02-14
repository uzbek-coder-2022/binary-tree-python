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


def get_min(root):
    if root.left is None:
        return root.val
    return get_min(root.left)

def get_max(root):
    if root.right is None:
        return root.val
    return get_min(root.right)

mn = 10**5 + 1
mx = 0

def get_minimum(root):
    global mn
    if root is not None:
        mn = min(root.val, mn)
        get_minimum(root.left)
        get_minimum(root.right)
        
def get_maximum(root):
    global mx
    if root is not None:
        mx = max(root.val, mx)
        get_minimum(root.left)
        get_minimum(root.right)
        

root = Node(13)
new_nodes = [7, 2, 9, 19]

for i in new_nodes:
    insert(root, i)
    

get_minimum(root)
get_maximum(root)
    
print(mn, mx)