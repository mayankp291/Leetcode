# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs for each path and keep track of max and min, time and space O(n)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mini, maxi):
            if not node:
                return abs(maxi-mini)
            mini = min(node.val, mini)
            maxi = max(node.val, maxi)
            return max(dfs(node.left, mini, maxi), dfs(node.right, mini, maxi))
        return dfs(root, root.val, root.val)