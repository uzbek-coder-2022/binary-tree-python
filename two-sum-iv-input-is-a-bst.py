# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode], dc):
        if root is None:
            return
        self.inorder(root.left, dc)
        if root.val not in dc:
            dc[root.val] = 1
        self.inorder(root.right, dc)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node_dict = {}
        self.inorder(root, node_dict)
        print(node_dict)
        for i in node_dict.keys():
            if k - i in node_dict and k - i != i:
                return True

        return False
