# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = []
        res1 = []
        res2 = []
        p1 = root1
        p2 = root2
        stack.append(root1)
        # inorder traversal for both trees and store the leaf nodes
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res1.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        stack.append(root2)
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res2.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return res1 == res2