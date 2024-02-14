class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None
        
root = Node(10)
print(root.val)
