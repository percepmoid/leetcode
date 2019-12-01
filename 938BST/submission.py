# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        def search(node):
            if node:
                if L <= node.val <= R:
                    self.sum += node.val
                if L < node.val:
                    search(node.left)
                if R > node.val:
                    search(node.right)
        search(root)
        return self.sum
    
